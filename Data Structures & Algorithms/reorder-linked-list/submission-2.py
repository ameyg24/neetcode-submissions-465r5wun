# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            print(second.val)
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        res = curr1 = head
        print(prev.val)
        curr2 = prev
        while curr1 and curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr2 = tmp2
            curr1 = tmp1
        # return head