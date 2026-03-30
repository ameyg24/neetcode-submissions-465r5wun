# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        ans = fast = slow = ListNode(0, head)
        def sorter(slow, fast, k):
            prev = fast.next
            curr = slow.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = slow.next
            slow.next = prev # can use prev
            return tmp
        while True:
            for _ in range(k):
                fast = fast.next
                if not fast:
                    return ans.next
            slow = fast = sorter(slow, fast, k)
        return ans.next
            
                