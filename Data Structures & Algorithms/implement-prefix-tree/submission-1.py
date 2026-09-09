class TrieNode: 
    def __init__(self): 
        self.children = {} 
        self.word = None



class PrefixTree:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        currNode = self.root

        for letter in word: 
            if not letter in currNode.children: 
                currNode.children[letter] = TrieNode()

            currNode = currNode.children[letter] 

        currNode.word = word
               

    def search(self, word: str) -> bool:
        currNode = self.root 

        for letter in word: 
            if not letter in currNode.children: 
                return False

            currNode = currNode.children[letter]

        return currNode.word == word
        

    def startsWith(self, prefix: str) -> bool:

        currNode = self.root 

        for letter in prefix: 
            if not letter in currNode.children: 
                return False

            currNode = currNode.children[letter]

        return True 
       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)