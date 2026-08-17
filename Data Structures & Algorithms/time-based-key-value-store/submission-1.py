from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if(self.hashMap[key][-1][0] < timestamp): 
            return ""
        
        left = 0 
        right = len(self.hashMap[key]) 
        nums = self.hashMap[key]

        while(left <= right): 
            mid = left + (right-left)//2 
          

            if(nums[mid][0] <= timestamp): 
                left = mid

            else: 
                right = mid-1

        return str(nums[left][1])


