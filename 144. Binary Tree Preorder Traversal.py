# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/description/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        def preorder(root):
            if root is None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        return res

    def preorder_iterative(self, root):
        if root is None:
            return
        stack = list()
        stack.append(root)
        res = []
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res
