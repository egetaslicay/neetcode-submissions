class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 
        parens = []

        def backtrack(i, numOpens): 
            if i == 2*n and numOpens == 0: 
                res.append("".join(parens.copy()))
                return res 

            if (n*2 - numOpens - i -1) > 0: 
                parens.append("(")
                backtrack(i+1, numOpens+1)
                parens.pop() 

            if(numOpens > 0):
                parens.append(")")
                backtrack(i+1, numOpens-1)
                parens.pop() 

        backtrack(0, 0)
        return res 

