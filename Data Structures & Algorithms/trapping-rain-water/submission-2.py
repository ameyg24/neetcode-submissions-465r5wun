class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # l = 0
        # curr = []
        # res = 0
        # for r in range(n):
        #     if height[r] >= height[l]:
        #         minval = min(height[r], height[l])
        #         while curr:
        #             x = curr.pop()
        #             print((minval-x))
        #             res += (minval-x)
        #         l = r
        #     else:
        #         curr.append(height[r])
        # return res
        n = len(height)
        maxleft = [0]*n
        maxright = [0]*n
        maxleft[0] = 0
        maxright[-1] = 0
        for i in range(1, n):
            maxleft[i] = max(height[i-1],maxleft[i-1])
        for i in range(n-2,-1,-1):
            maxright[i] = max(height[i+1], maxright[i+1])
        print(maxleft)
        print(maxright)
        minvals= [0]*n
        res = 0
        for i in range(n):
            minvals[i] = min(maxleft[i],maxright[i])
            res += (minvals[i] - height[i]) if (minvals[i] - height[i]) > 0 else 0
        return res
# 0 1 0 2 1 0 1 3 2 1 2 1


