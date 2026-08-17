class Solution:
    def isValid(self, s: str) -> bool:
        # set hashMap
        closeToOpen = {} 
        closeToOpen[']'] = '['
        closeToOpen['}'] = '{'
        closeToOpen[')'] = '('

        stack = []

        for char in s: 
            if char in closeToOpen: 
                if stack and stack[0] == closeToOpen[char]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)

        if stack: 
            return False

        return True
        

            
                



    
