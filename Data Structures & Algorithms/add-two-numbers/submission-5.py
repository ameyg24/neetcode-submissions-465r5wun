# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = res = ListNode(0)
        buf = 0
        while l1 and l2:
            tmp = l1.val + l2.val + buf
            buf = 0
            if tmp >= 10:
                tmp -= 10
                buf +=1
            res.next = ListNode(tmp)
            l1 = l1.next
            l2 = l2.next
            res = res.next
        while l1:
            tmp = l1.val + buf
            buf = 0
            if tmp >= 10:
                tmp -= 10
                buf +=1
            res.next = ListNode(tmp)
            res = res.next
            l1 = l1.next
        while l2:
            tmp = l2.val + buf
            buf = 0
            if tmp >= 10:
                tmp -= 10
                buf +=1
            res.next = ListNode(tmp)
            res = res.next
            l2 = l2.next
        if buf > 0:
            res.next = ListNode(buf)
        return ans.next      