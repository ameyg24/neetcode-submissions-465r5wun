# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        str1 = ""
        while first:
            str1 += (str(first.val))
            first = first.next
        second = l2
        str2 = ""
        while second:
            str2 += (str(second.val))
            second = second.next
        str1 = str1[::-1]
        str2 = str2[::-1]
        str3 = str(int(str1) + int(str2))
        str3 = str3[::-1]
        print(str3)
        head = ListNode(int(str3[0]))
        res = head
        for i in range(1, len(str3)):
            tmp = ListNode(int(str3[i]))
            res.next = tmp
            res = res.next
        return head

               