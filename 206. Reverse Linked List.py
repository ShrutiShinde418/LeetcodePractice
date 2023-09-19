# Problem: https://leetcode.com/problems/reverse-linked-list/description/

# Definition of a ListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = r = head
        q = None
        while p:
            r = p.next
            p.next = q
            q = p
            p = r
        return q
