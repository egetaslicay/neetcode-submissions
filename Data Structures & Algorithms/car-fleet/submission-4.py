class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = sorted(zip(position, speed), reverse=True)          
        times = []
        fleets = [] 

        for pos, sp in sortedCars: 
            time = (target - pos) / sp
            times.append(time)

        
        for time in times: 
            if fleets and time <= fleets[-1]:
                continue

            fleets.append(time)

        return len(fleets)
