class MedianFinder:
    # small is a max heap with negative numbers 

    def __init__(self):
        self.large = [] 
        self.small = [] 

    def addNum(self, num: int) -> None:
        if not self.small or num <= -1*self.small[0]: 
            heapq.heappush(self.small, -num)
        else: 
            heapq.heappush(self.large, num)

        if abs(len(self.small) - len(self.large)) > 1: 
            popped = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, popped)

        if(len(self.large) > len(self.small)): 
            popped = -1*heapq.heappop(self.large)
            heapq.heappush(self.small, popped)
        

    def findMedian(self) -> float:
        if len(self.large) == len(self.small): 
            return (self.large[0] + -1*(self.small[0])) / 2
        else: 
            return -1*self.small[0]
        
        