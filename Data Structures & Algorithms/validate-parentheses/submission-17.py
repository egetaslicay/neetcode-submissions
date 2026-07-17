class Solution:
    def isValid(self, s: str) -> bool:
        # set hashMap
        closeToOpen = {} 
        closeToOpen[']'] = '['
        closeToOpen['}'] = '{'
        closeToOpen[')'] = '('

        stack = deque()

        for char in s: 
            if char in closeToOpen: 
                if stack and stack[0] == closeToOpen[char]: 
                    stack.popleft()
                else: 
                    return False
            else: 
                stack.appendleft(char)

        if stack: 
            return False

        return True
        

            
                



    
