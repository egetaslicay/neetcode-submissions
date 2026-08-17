class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)

        while left < right: 
            if(numbers[left] + numbers[right] > target): 
                right -= 1
                continue

            if(numbers[left] + numbers[right] < target): 
                left += 1 
                continue

    
        return [left + 1, right + 1]

