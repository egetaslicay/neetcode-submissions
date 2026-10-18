class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1

        while left < right: 
            currSum = numbers[left] + numbers[right]

            if currSum > target: 
                right = right - 1 
            elif currSum < target: 
                left = left + 1 
            else: 
                return [numbers[left], numbers[right]]

        return [-1]
