# Problem: https://leetcode.com/problems/middle-of-the-linked-list/


class Solution:

    # time complexity: O(n)
    # space complexity: O(1)

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
