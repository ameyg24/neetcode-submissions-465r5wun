class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = s1.lower()
        s2 = s2.lower()
        count1 = {i : 0 for i in range(26)}
        count2 = {i : 0 for i in range(26)}
        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord("a")
            idx2 = ord(s2[i]) - ord("a")
            count1[idx1] += 1
            count2[idx2] += 1
        matches = 0
        for i in range(26):
            matches += 1 if count1[i] == count2[i] else 0
        l = 1
        for r in range(len(s1), len(s2)):
            print(matches,r,l)
            if matches == 26:
                return True
            idxr = ord(s2[r]) - ord("a")
            if count2[idxr] == count1[idxr]:
                matches -=1
            count2[idxr] += 1
            if count2[idxr] == count1[idxr]:
                matches += 1
            idxl = ord(s2[l-1]) - ord("a")
            if count2[idxl] == count1[idxl]:
                matches-=1
            count2[idxl] -=1
            if count2[idxl] == count1[idxl]:
                matches +=1
            # else:
            #     if count2[idxl] + 1 == count1[idxl]:
            #         matches -=1
            l+=1
        # print(matches)
        # print(count1)
        # print(count2)
        return matches == 26
