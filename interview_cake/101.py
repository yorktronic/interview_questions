# I'm making a search engine called MillionGazillion
# I wrote a crawler that visits web pages, stores a few keywords in a database, and follows links to other web pages.
# I noticed that my crawler was wasting a lot of time visiting the same pages over and over, so I made a set, visited,
# where I'm storing URLs I've already visited. Now the crawler only visits a URL if it hasn't already been visited.
# Thing is, the crawler is running on my old desktop computer in my parents' basement
# (where I totally don't live anymore), and it keeps running out of memory because visited is getting so huge.
# How can I trim down the amount of space taken up by visited?

# My solution
from urlparse import urlparse

VISITED = {}
VISITED_NESTED = {}

def store_url(url):
    # takes in a url, cleans domain and returns domain and path separately
    # won't handle subdomains, and a number of other things that would break this shit
    u = urlparse(url)
    netloc = u.netloc
    if 'www.' in netloc:
        netloc = netloc.replace('www.', '', 1)
    if netloc not in VISITED:
        VISITED[netloc] = []
    VISITED[netloc].append(u.path)

# Interview Cake's solution
class Trie:
    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):

        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes
        # as needed, and keeping track of whether we add
        # any nodes.
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        # Explicitly mark the end of a word.
        # Otherwise, we might say a word is
        # present if it is a prefix of a different,
        # longer word that was added earlier.
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word
