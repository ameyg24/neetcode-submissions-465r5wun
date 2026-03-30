# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        curr = root
        q = collections.deque()
        q.append(curr)
        while q:
            for _ in range(len(q)):
                tmp = q.popleft()
                if tmp:
                    res.append(str(tmp.val))
                else:
                    res.append("N")
                if tmp: q.append(tmp.left)
                if tmp: q.append(tmp.right)
        string = ",".join(res)
        print(string)
        return string

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array = data.split(",")
        print(array)
        if data[0] == "N":
            return None
        root = TreeNode(int(array[0]))
        q = collections.deque()
        q.append(root)
        i = 1
        while q:
            node = q.popleft()
            if array[i] != "N":
                node.left = TreeNode(int(array[i]))
                q.append(node.left)
            i+=1
            if array[i] != "N":
                node.right = TreeNode(int(array[i]))
                q.append(node.right)
            i+=1
        return root
