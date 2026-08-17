class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = sorted(zip(position, speed), reverse=True) 
        timesTaken = []

        for pos, speed in sortedCars: 
            time = (target - pos) / speed
            timesTaken.append(time)
        
        for time in timesTaken: 
            
            if stack and time <= stack[-1]: 
                continue
            else: 
                stack.append(time)

        return len(stack)                