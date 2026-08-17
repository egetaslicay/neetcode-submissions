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
                if stack and stack.pop() != closeToOpen[char]: 
                    return False
            else: 
                stack.append(char)

        return not stack 
        

            
                



    
