class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque() 
        visited = set(deadends)
        numTurns = 0 

        if "0000" in visited: 
            return -1 

        queue.append("0000")
        
        while queue: 
            numToPop = len(queue)

            for i in range(numToPop): 
                state = queue.popleft() 

                if state in visited: 
                    continue 

                visited.add(state)
            
                if state == target: 
                    return numTurns 

                for i in range(4): 

                    # turn it up
                    if state[i] == '9': 
                        turnUp = state[0:i] + '0' + state[i+1:]
                    else: 
                        newNum = str(int(state[i]) + 1)
                        turnUp = state[0:i] + newNum + state[i+1:]
                    
                   
                    # turn it down
                    if state[i] == '0': 
                        turnDown = state[0:i] + '9' + state[i+1:]
                    else: 
                        newNum = str(int(state[i]) - 1)
                        turnDown = state[0:i] + newNum + state[i+1:]
                    
                    queue.append(turnUp)
                    queue.append(turnDown)

            numTurns += 1 


        return -1 


                
