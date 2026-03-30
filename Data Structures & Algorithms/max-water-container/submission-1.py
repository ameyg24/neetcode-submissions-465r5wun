class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxarea = 0
        while left < right:
            mins = min(heights[right],heights[left])
            currarea = (right - left)*mins
            maxarea = max(maxarea, currarea)
            if mins == heights[right]:
                right -= 1
                while left< right and heights[right] < mins:
                    right -=1
            else:
                left += 1
                while left < right and heights[left] < mins:
                    left +=1     
        return maxarea   