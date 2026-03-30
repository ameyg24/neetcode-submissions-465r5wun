class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for el in strs:
            ans = ans + el + "-"
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        word = ""
        for char in s:
            if char == "-":
                ans.append(word)
                word = ""
            else:
                word += char
        return ans