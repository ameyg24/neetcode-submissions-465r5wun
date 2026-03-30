class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst = []
        for char in s:
            # if char in HashMap:
            #     HashMap[char] += 1
            # else:
            #     HashMap[char] = 1
            lst.append(char)
        for char in t:
            if char in lst:
                lst.remove(char)
        print(lst)
        return len(lst) == 0
        