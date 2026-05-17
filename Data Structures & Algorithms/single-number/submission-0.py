class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = set()
        for el in nums:
            if el not in visited:
                visited.add(el)
            else:
                visited.remove(el)
        return visited.pop()