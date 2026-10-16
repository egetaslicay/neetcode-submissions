class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs(i, path, total): 
            if total == target: 
                res.append(path.copy())
                return 

            if i >= len(candidates) or total > target: 
                return 

            # take this one 
            
            path.append(candidates[i])
            dfs(i+1, path, total + candidates[i]) 
            path.pop() 

            # skip this number 
            currNum = candidates[i] 
            i += 1 

            while i < len(candidates) and candidates[i] == currNum:
                i += 1

            if i < len(candidates): 
                dfs(i, path, total) 


        candidates.sort() 
        dfs(0, [], 0)

        return res 




        
