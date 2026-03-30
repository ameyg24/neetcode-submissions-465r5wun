class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""
        def dfs(left, right, curr):
            if right == left == n:
                res.append(curr[:])
                return
            if left == n:
                curr += ")"
                dfs(left, right+1, curr)
            elif left == right:
                curr += "("
                dfs(left + 1, right, curr)
            elif left > right:
                tmp = curr
                curr += "("
                dfs(left + 1, right, curr)
                curr = tmp          
                curr += ")"
                dfs(left, right + 1, curr)
        dfs(0,0, "")
        return res