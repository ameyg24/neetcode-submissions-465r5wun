class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = {}
        for index, value in enumerate(numbers):
            answer[value] = index
        print(answer)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers and i != answer[diff]:
                return([i + 1, answer[diff] + 1])
                