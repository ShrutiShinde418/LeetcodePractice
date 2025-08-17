# Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = ListNode(data)

        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new


def print_list(head):
    if not head:
        return

    p = head
    while p:
        print(p.val, end=" ")
        p = p.next
    print()


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


if __name__ == "__main__":
    arr1 = [1, 2, 4]
    arr2 = [1, 3, 4]
    llist1 = LinkedList()
    llist2 = LinkedList()
    for i in arr1:
        llist1.insert(i)
    for i in arr2:
        llist2.insert(i)
    ob = Solution()
    new_head = ob.mergeTwoLists(llist1.head, llist2.head)
    print_list(new_head)
