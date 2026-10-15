class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        array = self.map[key] 
        left = 0 
        right = len(array)-1
        res = "" 
       
        while(left <= right): 
            mid = (left + right) // 2

            if(array[mid][0] <= timestamp): 
                left = mid + 1  
                res = array[mid][1]

            elif(array[mid][0] > timestamp): 
                right = mid - 1
            else: 
                return array[mid][1]

        return res 
            
