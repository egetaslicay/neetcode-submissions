class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0 

        while(True): 
            fast = nums[nums[fast]]
            slow = nums[slow]

            if (fast == slow): 
                break

        # first cycle found
        secondSlow = 0 

        while(secondSlow != slow): 
            secondSlow = nums[secondSlow]
            slow = nums[slow]

        return slow
