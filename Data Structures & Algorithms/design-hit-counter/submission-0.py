class HitCounter:
    def __init__(self):
        self.times = [0] * 300 
        self.counts = [0] * 300 

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300 

        if self.times[i] == timestamp: 
            self.counts[i] += 1
        else: 
            self.counts[i] = 1
            self.times[i] = timestamp 
    

    def getHits(self, timestamp: int) -> int:
        sum = 0 

        for i in range(300): 
            if timestamp - self.times[i] < 300: 
                sum += self.counts[i]
                
        return sum 