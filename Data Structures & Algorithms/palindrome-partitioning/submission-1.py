class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        path = [] 
        

        def dfs(index: int) -> None: 
            if index == len(s): 
                res.append(path.copy())
                return 

            for j in range(index, len(s)): 
                piece = s[index:j+1]

                if piece == piece[::-1]: 
                    path.append(piece) 
                    dfs(j + 1)
                    path.pop() 

        dfs(0)


        return res 