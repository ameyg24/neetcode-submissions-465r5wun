# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            list.append(root.val)
            helper(root.right)
        helper(root)
        return list
        # string = self.helper(root)
        # for number in string.split("\n"):
        #     list.append(number)
        # return list
        # return self.helper(root)
    # def helper(self, root):
    #     if not root:
    #         return
    #     self.helper(root.left)
    #     print(root.val)
    #     self.helper(root.right)
        # return list
