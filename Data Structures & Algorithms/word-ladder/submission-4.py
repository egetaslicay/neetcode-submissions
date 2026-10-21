class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: # we need to be able to transform to endWord somehow 
            return 0 

        neighbours = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList: 
            for j in range(len(word)): 
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1 

        while queue: 
            numToPop = len(queue)

            for i in range(numToPop): 
                poppedWord = queue.popleft() 
                
                if poppedWord == endWord:
                    return res 

                for j in range(len(poppedWord)): 
                    pattern = poppedWord[:j] + "*" + poppedWord[j+1:]
                    
                    for neighbour in neighbours[pattern]: 
                        if neighbour not in visited: 
                            visited.add(neighbour)
                            queue.append(neighbour)

            res += 1 

        return 0 