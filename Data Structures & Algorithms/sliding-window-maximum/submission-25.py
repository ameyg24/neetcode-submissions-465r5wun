from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums): return []
        q = deque()
        for i in range(k):
            if not q:
                q.append(i)
            elif nums[q[-1]] > nums[i]:
                q.append(i)
            else:
                while q and nums[i] >= nums[q[-1]]:
                    q.pop()
                q.append(i)
        l = 0
        stack = [nums[q[0]]]
        for r in range(k, len(nums)):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            l+=1
            if l > q[0]:
                q.popleft()
            stack.append(nums[q[0]])

        return stack
        # l = 0
        # for r in range(k, len(nums)):
