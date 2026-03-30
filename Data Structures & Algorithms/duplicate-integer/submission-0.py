class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashMap = {}
        for el in nums:
            if el in HashMap:
                return True
            else:
                HashMap[el] = 1
        return False
        
        