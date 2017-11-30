# Datatron interview question

## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

#F
#/ \
#   B
#H
#/  \ /
#A
#D
#G
#/ \
#    C
# E

# Turn tree in to circular doubly-linked-list

# A <-> B <-> C <-> D <-> F <-> G <-> H <-> A

# F -> B
# B -> A

# A <-> F

def build_cdll(root):
    # in: root of a tree
    # out: head

    if root.left == None and root.right == None:
        # we've found the head of the CDLL
    elif root.left == None and root.right is not None:
        # we've found the head and the next element may be root.right
        build_cdll(root.right)
    elif root.left is not None and root.right is None:
        build_cdll(root.left)

    build_cdll(root.left)
