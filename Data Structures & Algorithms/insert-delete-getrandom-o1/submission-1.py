class RandomizedSet:

    def __init__(self):
        self.numToIndex = {} 
        self.nums = [] 

    def insert(self, val: int) -> bool:
        if val not in self.numToIndex: 
            self.numToIndex[val] = len(self.nums)
            self.nums.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.numToIndex:
            indexToPut = self.numToIndex[val]
            toInsert = self.nums[-1]
            self.nums[indexToPut] = toInsert 
            self.numToIndex[toInsert] = indexToPut
            self.nums.pop()
            del self.numToIndex[val]
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