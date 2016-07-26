def wiki_common_words(wiki_entry_title):
    import wikipedia
    ml = wikipedia.page(wiki_entry_title).content

    # Remove punctuation from string
    punctuation = ['!', '.', ',', ':', ';', '?', '=', '/', "'", '"', '}', '{', '[', ']', '%', '$', '(', ')']

    # add common word removal here -- had an issue installing nltk so hopefully this part works
    from nltk.corpus import stopwords
    c = list(stopwords.words('english'))

    ml = "".join(s for s in ml if s not in punctuation)

    # Replace any occurances of \n with a space
    ml = ml.replace('\n', " ")

    # Replace any double spaces with a single space
    ml = ml.replace('  ', ' ')

    # Split ml on spaces into a list of words
    ml_words = ml.split(" ")

    words = {}

    for word in ml_words:
        # Remove common words while creating the dictionary
        if word not in c:
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 0

    # Get the n most common words
    n = 10

    import operator
    sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_words[:n]

