class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isMirror(self, l, r):
        if l is None and r is None:
            return True

        if l is not None and r is not None and l.val == r.val:
            return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)

        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isMirror(root.left, root.right)


s = Solution()

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(2)

tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(4)

tree1.right.left = TreeNode(4)
tree1.right.right = TreeNode(3)

assert (s.isSymmetric(tree1) == True)

assert (s.isSymmetric(None) == True)

tree2 = TreeNode(2)
tree2.left = TreeNode(3)
tree2.right = TreeNode(3)

tree2.left.left = TreeNode(4)
tree2.left.right = TreeNode(5)

tree2.right.left = TreeNode(None)
tree2.right.right = TreeNode(4)

assert (s.isSymmetric(tree2) == False)