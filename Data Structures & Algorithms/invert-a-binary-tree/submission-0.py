# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def helper(root):
        #     tmp = root.left
        #     root.left = root.right
        #     root.right = root.left
        # def swap(root):
        #     if not root:
        #         return
        #     helper(root)
        #     swap(root.left)
        #     swap(root.right)
        if not root:
            return None
        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        

        