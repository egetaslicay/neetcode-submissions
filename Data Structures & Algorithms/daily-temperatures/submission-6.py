class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  

        for i in range(len(temperatures)):

            while(stack and temperatures[i] >= temperatures[stack[-1]]): 
                res[stack.pop()] = (i - stack.pop())


            stack.append(i)

        res.append(0)        

        return res
