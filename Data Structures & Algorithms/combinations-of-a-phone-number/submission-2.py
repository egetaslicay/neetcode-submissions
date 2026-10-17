class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberToLetters = defaultdict(list)
        numberToLetters[2] = ["a", "b", "c"]
        numberToLetters[3] = ["d", "e", "f"]
        numberToLetters[4] = ["g", "h", "i"]
        numberToLetters[5] = ["j", "k", "l"]
        numberToLetters[6] = ["m", "n", "o"]
        numberToLetters[7] = ["p", "q", "r", "s"]
        numberToLetters[8] = ["t", "u", "v"]
        numberToLetters[9] = ["w", "x", "y", "z"]

        res = [] 
        path = [] 

        if not digits: 
            return res 

        def dfs(i: int) -> None: 
            if i == len(digits):
                res.append("".join(path.copy()))
                return 

            for letter in numberToLetters[int(digits[i])]:
                path.append(letter)
                dfs(i + 1)
                path.pop() 

        dfs(0) 

        return res
                