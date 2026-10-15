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

                for j in range(4): 

                    # turn it up
                    if state[j] == '9': 
                        turnUp = state[0:j] + '0' + state[j+1:]
                    else: 
                        newNum = str(int(state[j]) + 1)
                        turnUp = state[0:j] + newNum + state[j+1:]
                    
                   
                    # turn it down
                    if state[j] == '0': 
                        turnDown = state[0:j] + '9' + state[j+1:]
                    else: 
                        newNum = str(int(state[j]) - 1)
                        turnDown = state[0:j] + newNum + state[j+1:]
                    
                    queue.append(turnUp)
                    queue.append(turnDown)

            numTurns += 1 


        return -1 


                
