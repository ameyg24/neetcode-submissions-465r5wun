# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        res = []
        def construct(preorder, inorder):
            if not preorder or not inorder:
                return None
            mid = preorder[0]
            idx = inorder.index(mid)
            curr = TreeNode(mid)
            curr.left = construct(preorder[1:idx+1], inorder[:idx])
            curr.right = construct(preorder[idx+1:], inorder[idx+1:])
            return curr
        return construct(preorder, inorder)