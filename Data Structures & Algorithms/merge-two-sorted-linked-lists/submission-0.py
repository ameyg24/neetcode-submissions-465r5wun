# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 cases, either first is bigger, or second is bigger.
        # if first is bigger, input first to new list
        head = ListNode(-1)
        tmp = head
        curr1 = list1
        curr2 = list2
        while list1 or list2:
            if list1 == None and list2 != None:
                tmp.next = list2
                list2 = list2.next
                tmp = tmp.next
            elif list2 == None and list1 != None:
                tmp.next = list1
                list1 = list1.next
                tmp = tmp.next
            elif list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
                tmp = tmp.next
            else:
                tmp.next = list2
                list2 = list2.next
                tmp = tmp.next
        return head.next

        