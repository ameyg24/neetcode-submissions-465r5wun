class Solution:
    def isValid(self, s: str) -> bool:
        maps = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for char in s:
            if char not in maps:
                stack.append(char)
            elif char in maps and stack:
                tmp = stack.pop()
                if tmp != maps[char]:
                    return False
            else:
                return False
        return len(stack) == 0
            