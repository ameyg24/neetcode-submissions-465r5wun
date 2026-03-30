class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match = defaultdict(list)
        if not digits:
            return []
        match["0"] = ["+"]
        match["1"] = [""]
        match["2"] = ["A","B","C"]
        match["3"] = ["D","E","F"]
        match["4"] = ["G","H","I"]
        match["5"] = ["J","K","L"]
        match["6"] = ["M","N","O"]
        match["7"] = ["P","Q","R","S"]
        match["8"] = ["T","U","V"]
        match["9"] = ["W","X","Y","Z"]
        match["*"] = ["*"]
        match["#"] = ["#"]
        res = []
        curr = ""
        def dfs(i):
            nonlocal curr
            if i == len(digits):
                res.append(curr)
                return
            for el in match[digits[i]]:
                curr += el.lower()
                dfs(i+1)
                curr = curr[:-1]
        dfs(0)
        return res
