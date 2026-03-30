
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxcounts = []
        q = deque()
        l=0
        for r in range(k):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
        maxcounts.append(nums[q[0]])
        for r in range(k, len(nums)):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            l+=1
            if q[0] < l:
                q.popleft()
            maxcounts.append(nums[q[0]])
        # print(q)
        return maxcounts

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         output = []
#         q = deque()  # index
#         l = r = 0

#         while r < len(nums):
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop()
#             q.append(r)

#             if l > q[0]:
#                 q.popleft()

#             if (r + 1) >= k:
#                 output.append(nums[q[0]])
#                 l += 1
#             r += 1

#         return output

       