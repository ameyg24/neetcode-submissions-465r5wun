class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(n-1, -1, -1):
            for w in wordDict:
                if len(w) + i > n:
                    continue
                else:
                    if s[i:i + len(w)] == w and not dp[i]:
                        dp[i] = dp[i + len(w)]
        return dp[0]