# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/description/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        current = root
        stack = list()
        res = list()
        if root is None:
            return
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                res.append(current.val)
                current = current.right
            else:
                break
        return res

    def inorder_recursive(self, root):
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res
