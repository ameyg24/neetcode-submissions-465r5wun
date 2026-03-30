# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sorter(a: Optional[ListNode], b: Optional[ListNode]):
            ans = res = ListNode(0)
            while a and b:
                if a.val <= b.val:
                    res.next = ListNode(a.val)
                    a = a.next
                else:
                    res.next = ListNode(b.val)
                    b = b.next
                res = res.next
            if a: res.next = a
            if b: res.next = b
            return ans.next
        def splitter(lists):
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]
            mid = len(lists)//2
            left = splitter(lists[:mid])
            right = splitter(lists[mid:])
            return sorter(left, right)
        return splitter(lists)