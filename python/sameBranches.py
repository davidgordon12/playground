class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric( root: TreeNode) -> bool:
    def compare(left, right) -> bool:
        if not left or not right:
            return left == right
        else:
            return left.val == right.val and compare(left.left, right.left) and compare(left.right, right.right)

    return compare(root.left, root.right)


tree1 = TreeNode(9, TreeNode(1, TreeNode(5), TreeNode(2)), TreeNode(1, TreeNode(5), TreeNode(2)))

print(isSymmetric(tree1))
