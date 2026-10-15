class RandomizedSet:

    def __init__(self):
        self.numToIndices = defaultdict(set)
        self.nums = [] 
        

    def insert(self, val: int) -> bool:
        wasThere = not val in self.numToIndices
        
        index = len(self.nums)
        self.nums.append(val)
        self.numToIndices[val].add(index)

        return wasThere

    def remove(self, val: int) -> bool:
        if val in self.numToIndices: 
            lastIndex = len(self.nums)-1
            indexToInsert = self.numToIndices[val].pop()  # where your hole is 
            valToInsert = self.nums[lastIndex] # value at the end of the array 

            self.nums[indexToInsert] = valToInsert 
            self.numToIndices[valToInsert].add(indexToInsert) # 

            self.nums.pop() # pop thatt value 
            self.numToIndices[valToInsert].remove(lastIndex)

            if(not self.numToIndices[val]): 
                del self.numToIndices[val]

            return True

        return False 
        

    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.nums)-1)
        return self.nums[randomIndex]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

""" Implement a RandomizedCollection, a multiset of integers where the same value can appear more than once.

RandomizedCollection(): creates an empty collection.

insert(val) -> bool: adds one copy of val, even if its already there. Returns True if val was not present before this insert, and False if it already was.

remove(val) -> bool: removes one copy of val, if there is one. Returns True if a copy was removed, False if val wasnt present.

getRandom() -> int: returns a random element. The chance of each value is proportional to how many copies it has. Its only called when the collection isnt empty.""" 