
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        second = head
        for _ in range(n):
            second = second.next
        first = head
        prev = ListNode(0)
        prev.next = head
        res = prev
        while first and second:
            prev = first
            first = first.next
            second = second.next
        prev.next = prev.next.next
        return res.next