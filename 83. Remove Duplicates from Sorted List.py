# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    if head is None:
        return
    p = head
    while p:
        print(p.val, end=" ")
        p = p.next
    print()


class Solution:

    # time complexity: O(n)
    # space complexity: O(n)

    def deleteDuplicates(self, head):
        temp = curr = ListNode(0)
        s = set()
        while head is not None:
            if head.val not in s:
                curr.next = ListNode(head.val)
                s.add(head.val)
                curr = curr.next
            head = head.next

        return temp.next

    # time complexity: O(n)
    # space complexity: O(1)

    def delete_duplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3]
    llist1 = LinkedList()
    llist2 = LinkedList()
    for i in arr:
        llist1.insert(i)
        llist2.insert(i)
    ob = Solution()
    head1 = ob.delete_duplicates(llist1.head)
    print_list(head1)
    head2 = ob.deleteDuplicates(llist2.head)
    print_list(head2)
