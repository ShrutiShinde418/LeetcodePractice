# Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/description/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def postorderTraversal(self, root: [TreeNode]) -> [int]:
        def postorder(root):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = []
        postorder(root)
        return res

    def postorder_iterative(self, root):
        if root is None:
            return
        res = []
        s1 = list()
        s2 = list()
        s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            node = s2.pop()
            res.append(node.val)
        return res
