from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.hashMap[key]
        res = "" 
        if(not nums or nums[0][0] > timestamp): 
            return res 

        left = 0 
        right = len(nums)-1
        
        while(left < right): 
            mid = left + (right-left)//2 

            if(nums[mid][0] <= timestamp): 
                res = nums[mid][1]
                left = mid + 1 
            else: 
                right = mid - 1


        return res