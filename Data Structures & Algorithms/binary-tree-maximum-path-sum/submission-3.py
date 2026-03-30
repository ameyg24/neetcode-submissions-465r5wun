# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            left = max(0, dfs(curr.left))
            right = max(0, dfs(curr.right))
            res = max(res, curr.val + left + right)
            return curr.val + max(left, right)
        dfs(root)
        return res
# 5
# 4 8
# 11 null 13 4 
# 7 2 null null null 1