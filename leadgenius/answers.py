################################################################
#         ANSWERS TO LEADGENUIS INTERVIEW QUESTIONS            #
################################################################

# QUESTION 1: Given a square matrix, return the same matrix rotated 90 degress

# Solution 1, using pandas
import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def rotate_pandas(df):
    return df.T.reset_index().reindex(columns=[0, 1, 2])

# Solution 2, without pandas
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate(matrix):
    return [list(x) for x in zip(*matrix)]

# QUESTION 2: Given a graph, print out the contents of the graph line by line
tree = {0: [1],
        1: [2, 3],
        2: [4, None],
        3: [5, 6],
        4: [7, None],
        5: [None, None],
        6: [None, None],
        7: [8,9],
        8: [None, None],
        9: [None, None]}

# Recursive solution that Roman and I came up with together
def print_tree(tree, levels):
    if not levels: # If levels is None, return
        return
    children = []
    print levels
    for level in levels:
        if not level:
            continue
        leaf = tree[level]
        for item in leaf:
            if item is not None:
                children.append(item)
    print_tree(tree, children)

