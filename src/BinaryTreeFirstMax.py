class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def searching_first_biggest(root, node):
    if node.right:
        return leaf(node.right)
    elif node == node.parent.left:
        return node.parent.value
    elif node.value < root.value:
        return root.value
    else:
        return node.value


def leaf(node):
    if not node.left:
        return node.value
    return leaf(node.left)
