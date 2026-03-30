class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            tmp = i
            while stack and stack[-1][1] > h:
                tmp, height = stack.pop()
                maxarea = max(maxarea, (i-tmp)*height)
            stack.append((tmp,h))
        while stack:
            tmp, height = stack.pop()
            maxarea = max(maxarea, (len(heights)-tmp)*height)
        return maxarea
            