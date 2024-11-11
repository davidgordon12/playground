class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Prints each node
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        print(True)
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    print(False)
    return False


#       9
#    1
#   5 2
tree1 = TreeNode(9, TreeNode(1, TreeNode(5), TreeNode(2)))

#       9
#    1     7
#   5 2
tree2 = TreeNode(9, TreeNode(1, TreeNode(5), TreeNode(2)), TreeNode(7))

print("\nVerdict: " + str(isSameTree(tree1, tree2)))
