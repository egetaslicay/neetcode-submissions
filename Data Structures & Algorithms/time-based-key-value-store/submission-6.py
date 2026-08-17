from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if(self.hashMap[key][0][0] > timestamp): 
            return res
        
        left = 0 
        right = len(self.hashMap[key]) 
        nums = self.hashMap[key]
        res = 0

        while(left < right): 
            mid = left + (right-left)//2 
        
            if(nums[mid][0] <= timestamp): 
                res = nums[mid][0]
                left = mid+1
            else: 
                right = mid

        return str(res)


