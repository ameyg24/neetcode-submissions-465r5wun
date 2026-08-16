class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = []
        for i, el in enumerate(nums):
            index_map.append([el, i])
        index_map.sort()
        l = 0
        r = len(index_map) - 1
        while l < r:
            curr_sum = index_map[l][0] + index_map[r][0]
            if curr_sum == target:
                return [min(index_map[l][1], index_map[r][1]),max(index_map[l][1], index_map[r][1])]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
        return [-1,-1]