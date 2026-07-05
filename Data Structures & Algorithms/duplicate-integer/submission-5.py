class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        return not (len(my_set) == len(nums))
        