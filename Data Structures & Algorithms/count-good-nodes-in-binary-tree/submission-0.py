# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        maxval = root.val
        def inorder(root, maxval):
            nonlocal count
            if not root:
                return
            if root.val >= maxval:
                count += 1
            maxval = max(maxval, root.val)
            inorder(root.left, maxval)
            inorder(root.right, maxval)
            return count
        

        ans = inorder(root, maxval)
        return ans

        