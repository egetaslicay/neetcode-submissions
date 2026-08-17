class MinStack:

    def __init__(self):
        self.stack = []
        self.stack = [] 

    def push(self, val: int) -> None:
        if not minStack or val <= minStack[-1]: 
            minStack.append(val)

        stack.append(val)
        

    def pop(self) -> None:
        topVal = stack.pop() 
        if topVal == minStack[-1]: 
            minStack.pop() 


    def top(self) -> int:
        return stack[-1]

    def getMin(self) -> int:
        return minStack[-1]
