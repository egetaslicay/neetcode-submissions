class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.large and -1 * self.small[0] > self.large[0]: 
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * popped)

        if abs(len(self.large) - len(self.small)) > 1: 
            if len(self.large) > len(self.small):
                popped = heapq.heappop(self.large)
                heapq.heappush(self.small, -1 * popped)
            else: 
                popped = heapq.heappop(self.small)
                heapq.heappush(self.large, -1 * popped)

    def findMedian(self) -> float:
        if (len(self.large) + len(self.small)) % 2 == 0: 
            return (-1 * self.small[0] + self.large[0])/2
        else: 
            if len(self.large) > len(self.small): 
                return self.large[0]
            else: 
                return self.small[0] * -1
        
        