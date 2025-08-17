# Problem: https://leetcode.com/problems/reverse-linked-list/description/


# Definition of a ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new = ListNode(val)
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new


def print_list(head):
    p = head
    while p:
        print(p.val, end=" ")
        p = p.next
    print()


class Solution:

    # time complexity: O(n)
    # space complexity: O(1)

    def reverseList(self, head: ListNode) -> ListNode:
        p = r = head
        q = None
        while p:
            r = p.next
            p.next = q
            q = p
            p = r
        return q

    # time complexity: O(n)
    # space complexity: O(n)

    def reverse_list_recursive(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head

        rev_head = self.reverse_list_recursive(head.next)

        head.next.next = head
        head.next = None

        return rev_head

    # time complexity: O(n)
    # space complexity: O(n)

    def reverse_list(self, head: ListNode) -> ListNode:
        p = head
        stack = []
        while p.next:
            stack.append(p)
            p = p.next
        head = p
        while stack:
            p.next = stack.pop()
            p = p.next

        p.next = None
        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist3 = LinkedList()
    for i in arr:
        llist1.insert(i)
        llist2.insert(i)
        llist3.insert(i)
    ob = Solution()
    head1 = ob.reverse_list(llist1.head)
    head2 = ob.reverse_list_recursive(llist2.head)
    head3 = ob.reverseList(llist3.head)
    print_list(head1)
    print_list(head2)
    print_list(head3)
