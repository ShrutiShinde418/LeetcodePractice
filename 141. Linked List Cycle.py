# Problem: https://leetcode.com/problems/linked-list-cycle/description/


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
