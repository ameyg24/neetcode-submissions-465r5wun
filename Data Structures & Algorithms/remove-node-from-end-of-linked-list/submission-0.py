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
            lst.append(curr.val)
            curr = curr.next
        lst.pop(len(lst) - n)
        if len(lst) == 0:
            tmp = ListNode()
            return None
        he = ListNode(lst[0])
        ans = he
        for i in range(1, len(lst)):
            tmp = ListNode(lst[i])
            ans.next = tmp
            ans = ans.next
        return he
        # for i in range(len(lst) - 1):
        #     if i == len(lst) - n:
        #         if i == 0 and curr.next:
        #             curr = ListNode(curr.next.val)
        #         elif i == 0:
        #             return []
        #         else:
        #             curr = curr.next.next
        #     else:
        #         curr = curr.next
        # return curr