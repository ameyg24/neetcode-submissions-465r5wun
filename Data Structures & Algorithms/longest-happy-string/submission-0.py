import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxheap = "", []
        for count, char in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if count < 0:
                heapq.heappush(maxheap, (count, char))
        while maxheap:
            print(maxheap)
            count, char = heapq.heappop(maxheap)
            if len(res) > 1 and char == res[-1] == res[-2]:
                if maxheap:
                    count2, char2 = heapq.heappop(maxheap)
                    res += char2
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(maxheap, (count2, char2))
                else:
                    break
            else:
                res += char
                count += 1
            # else:
            #     break
            if count < 0:
                heapq.heappush(maxheap, (count, char))
        return res