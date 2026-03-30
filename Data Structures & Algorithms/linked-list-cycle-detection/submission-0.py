# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        lst = []
        while curr.next:
            lst.append(curr)
            curr = curr.next
            if curr in lst:
                return True
        return False
