# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # need to use inorder??
        lists = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            lists.append(root.val)
            helper(root.right)
        helper(root)
        print(lists)
        return lists[k - 1]
        