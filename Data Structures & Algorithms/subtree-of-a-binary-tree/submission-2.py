# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return check(root.left, subroot.left) and check(root.right, subroot.right)
            else:
                return False
        curr = root
        res = False
        def dfs(curr, sub):
            nonlocal res
            if not curr:
                return
            if curr.val == sub.val:
                res = check(curr, sub)
                if res == True:
                    return
            dfs(curr.left, sub)
            dfs(curr.right, sub)
        dfs(root, subRoot)
        return res




# """
#                 1
#             null 1
#         null 1 null 1
#     null 1 null 1 null 1 null 1
#         null 1 null 1 null 1 2