# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        if l > r:
            return l + 1
        else:
            return r + 1


s = Solution()

tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)

tree1.left.left = TreeNode(None)
tree1.left.right = TreeNode(None)

tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

assert (s.maxDepth(tree1) == 3)

