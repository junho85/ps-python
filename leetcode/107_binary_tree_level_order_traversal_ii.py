# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        result = []
        self.traverse(root, result, 0)
        result = list(reversed(result))
        return result

    def traverse(self, root: TreeNode, result, level):
        if root is None:
            return

        currlist = []
        if root.val is not None:
            if level < len(result):
                currlist = result[level]
            else:
                result.append(currlist)
            currlist.append(root.val)

        if root.left is not None:
            self.traverse(root.left, result, level + 1)

        if root.right is not None:
            self.traverse(root.right, result, level + 1)


s = Solution()

tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)

tree1.left.left = TreeNode(None)
tree1.left.right = TreeNode(None)

tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

result = s.levelOrderBottom(tree1)
print(result)
assert (result == [[15, 7], [9, 20], [3]])
