# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next
        res = []
        for i in range(len(lst)):
            length = len(lst)
            if i%2 == 0:
                res.append(lst[(i + 1)//2].val)
            else:
                res.append(lst[length-((i + 1)//2)].val)
        print(res)
        # head = ListNode(res[0])
        # curr = head
        # for i in range(1, len(res)):
        #     tmp = ListNode(res[i])
        #     curr.next = tmp
        #     curr = curr.next
        for i in range(length):
            lst[i].val = res[i]

        
        