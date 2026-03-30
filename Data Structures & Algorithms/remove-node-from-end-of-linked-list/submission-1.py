# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lst = []
        while curr:
            lst.append(curr)
            curr = curr.next
        index = len(lst) - n
        if index == 0:
            return head.next
        lst[index-1].next = lst[index].next
        return head