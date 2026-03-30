# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        plst = []
        while not curr.val == p.val:
            plst.append(curr)
            if p.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        plst.append(p)
        curr = root
        qlst = []
        while not curr.val == q.val:
            qlst.append(curr)
            if q.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        qlst.append(q)
        res = None
        minl = min(len(qlst), len(plst))
        for i in range(minl):
            if qlst[i].val == plst[i].val:
                res = qlst[i]
        print(qlst)
        print(plst)
        return res