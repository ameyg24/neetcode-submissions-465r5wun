class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(1, k+1):
                if (i + j) < len(nums) and nums[i] == nums[i+j]:
                    print(i, j)
                    return True
        return False