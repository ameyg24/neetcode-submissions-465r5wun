class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        s = nums[0]
        while s != fast:
            s = nums[s]
            fast = nums[fast]
        return s