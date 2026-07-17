class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for idx in range(n):
            for l in range(n):
                r = l + idx
                if r < n and s[l] == s[r] and r-l < 3:
                    dp[l][r] = True
                elif l + 1 < n and r < n and s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1]
        count = 0
        for _ in dp:
            count += sum(_)
        return count