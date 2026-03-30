# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # if (not root.right and not root.left):
        #     if key == root.val:
        #         return None
        #     else:
        #         return root
        # if not root.right or not root.left:
        #     if not root.left and root.val != key :
        #         root = self.deleteNode(root.right, key)
        #     if not root.left and root.val == key:
        #         root = root.right
        #     if not root.right and root.val == key:
        #         root = root.left
        #     if not root.right and root.val != key:
        #         root = self.deleteNode(root.left, key)
        #     return root
        if key > root.val:
            root.right =  self.deleteNode(root.right, key)
        if key < root.val:
            root.left =  self.deleteNode(root.left, key)
        if key == root.val: 
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                minval = self.minNode(root.right)
                root.val = minval
                root.right = self.deleteNode(root.right, minval)
        return root
    def minNode(self, root):
        tmp = root
        while tmp.left:
            tmp = tmp.left
        return tmp.val