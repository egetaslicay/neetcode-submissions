class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = {} 
        dependents = defaultdict(set)
        res = []

        for word in words: 
            for char in word: 
                if char not in indegree: 
                    indegree[char] = 0



        for i in range(len(words)-1): 
            word1 = words[i]
            word2 = words[i+1]
            
            if len(word1) > len(word2) and word1.startswith(word2): 
                return "" 

            idx = 0 

            while idx < min(len(word1),len(word2)): 
                letter1 = word1[idx]
                letter2 = word2[idx]
                idx += 1

                if letter1 != letter2:
                    if letter2 not in dependents[letter1]: 
                        indegree[letter2] += 1 
                        dependents[letter1].add(letter2)
                    break

        ready = [] 
        for letter, indeg in indegree.items(): 
            if indeg == 0: 
                ready.append(letter)

        while ready: 
            prevReady = ready.copy() 
            ready = [] 

            for letter in prevReady: 
                res.append(letter)
                for dependent in dependents[letter]: 
                    indegree[dependent] -= 1 
                    if indegree[dependent] == 0: 
                        ready.append(dependent)

        if len(res) != len(indegree): 
            return "" 

        return "".join(res)

                    
                    


