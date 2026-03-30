class Solution:
    def isValid(self, s: str) -> bool:
        maps = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in maps:
                stack.append(char)
            else:
                if not stack or stack[-1] != maps[char]:
                    return False
                stack.pop()
        return len(stack) == 0