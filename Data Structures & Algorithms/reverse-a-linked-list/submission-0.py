# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = head
        lst = []
        while values:
            lst.append(values.val)
            values = values.next
        # answer = ListNode(lst[-1])
        prev = ListNode(-1)
        curr =  prev
        for element in lst[::-1]:
            curr.next = ListNode(element)
            curr = curr.next
        return prev.next