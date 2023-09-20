# Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    # time complexity: O(m+n)
    # space complexity: O(1)
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        temp = dummy = ListNode(0)
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return dummy.next
