# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        if not pairs:
            return ans
        ans.append(pairs[:])
        # tmp = pairs[0].key
        # ans.append(pairs)
        for j in range(len(pairs) - 1):
            # copy = pairs
            if pairs[j].key > pairs[j + 1].key:
                i = j
                while pairs[i].key > pairs[i+1].key and i >= 0:
                    buff = pairs[i+1]
                    pairs[i+1] = pairs[i]
                    pairs[i] = buff
                    i -= 1
            ans.append(pairs[:])
        return ans

        