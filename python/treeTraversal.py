class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Prints each node
def Traverse(tree: TreeNode):
    if tree is None:
        return
    print(tree.val)
    Traverse(tree.left)
    Traverse(tree.right)


tree = TreeNode(9, TreeNode(1, None, TreeNode(2, None, None)), None)

Traverse(tree)
