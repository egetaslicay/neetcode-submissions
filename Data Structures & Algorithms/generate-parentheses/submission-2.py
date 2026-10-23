class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 
        path = [] 

        def dfs(index: int, numOpens: int): 
            if index == 2*n and numOpens == 0: 
                res.append("".join(path))
                return 


            if numOpens > 0: 
                path.append(")")
                dfs(index + 1, numOpens - 1)
                path.pop() 

            if 2*n - numOpens - index > 0:
                path.append("(")
                dfs(index + 1, numOpens + 1)
                path.pop() 

        dfs(0, 0)

        return res 

            
