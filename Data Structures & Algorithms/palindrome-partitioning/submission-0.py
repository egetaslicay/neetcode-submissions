class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = [] 
        res = [] 

        def dfs(i): 
            if i == len(s): 
                res.append(path.copy())
                return 


            for j in range(i+1, len(s)+1): 
                if s[i:j] == s[i:j][::-1]: 
                    path.append(s[i:j])
                    dfs(j) # maybe this should be j ?? 
                    path.pop() 
                


        dfs(0)
        return res 