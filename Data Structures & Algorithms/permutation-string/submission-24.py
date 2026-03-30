class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        count1 = {i:0 for i in range(26)}
        count2 = {i:0 for i in range(26)}
        for i in range(len(s1)):
            idx1 = ord(s1[i])-ord("a")
            count1[idx1] +=1
        for i in range(len(s1)):
            idx2 = ord(s2[i]) - ord("a")
            count2[idx2] +=1
        correct = 0
        k = len(s1)
        print(count1)
        print(count2)
        for i in range(26):
            if count1[i] == count2[i]:
                correct +=1
        print(correct)
        if correct == 26: return True
        l = 0
        for r in range(k, len(s2)):
            idx1 = ord(s2[r]) - ord("a")
            if count2[idx1] == count1[idx1]:
                correct-=1
            count2[idx1] += 1
            if count2[idx1] == count1[idx1]:
                correct +=1 
            idx2 = ord(s2[l]) - ord("a")
            if count2[idx2] == count1[idx2]:
                correct -= 1
            count2[idx2] -=1
            if count2[idx2] == count1[idx2]:
                correct +=1
            l+=1
            # idx3 = ord(s2[l])-ord("a")
            # if count2[idx3] == count1[idx3]:
            #     correct +=1
            print(correct)
            if correct == 26:
                return True
            # if count2[idx1] == count1[idx1] :
            #     correct -=1
            # count2[idx1]+=1
            # if count2[idx1] == count1[idx1]:
            #     correct +=1
            # idx2 = ord(s2[l]) - ord("a")
            # if count2[idx2] == count1[idx2]:
            #     correct -=1
            # count1[idx2]-=1
            # l+=1
            # idx3 = ord(s2[l]) - ord("a")
            # if count2[idx3] == count1[idx3] and idx3 == idx2:
            #     correct +=1
            # print(correct)
            # if correct == 26:
            #     return True
        return False


