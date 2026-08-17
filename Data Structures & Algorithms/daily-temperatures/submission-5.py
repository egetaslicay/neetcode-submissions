class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resStack = []
        stack = []  
        res = [] 

        for i in range(len(temperatures)):

            while(stack and temperatures[i] >= temperatures[stack[-1]]): 
                resStack.append(i - stack.pop())


            stack.append(i)

        for num in resStack: 
            res.append(resStack.pop())
        

        return res
