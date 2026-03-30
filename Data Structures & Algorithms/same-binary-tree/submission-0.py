# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            pleft = p.left
            pright = p.right
            qleft = q.left
            qright = q.right
            if p.val != q.val:
                return False
            else:
                return dfs(pleft, qleft) and dfs(pright, qright)
        return dfs(p,q)