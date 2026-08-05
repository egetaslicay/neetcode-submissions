class Node: 
    def __init__(self, key, val): 
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} 
        self.capacity = capacity 
        self.rightDummy = Node(0, 0)
        self.leftDummy = Node(0, 0)
        self.rightDummy.prev = self.leftDummy
        self.leftDummy.next = self.rightDummy 
        

    def get(self, key: int) -> int:
        if key in self.cache: 
            nodeToDisplace = self.cache[key]

            self.removal(nodeToDisplace)
            self.insertion(nodeToDisplace)
           
            return nodeToDisplace.val
        else:
            return -1


    def removal(self, nodeToRemove):
        nxt = nodeToRemove.next
        prv = nodeToRemove.prev
        nxt.prev = prv
        prv.next = nxt 


    def insertion(self, nodeToInsert):
        beforeRightDummy = self.rightDummy.prev
        beforeRightDummy.next = nodeToInsert
        nodeToInsert.prev = beforeRightDummy
        nodeToInsert.next = self.rightDummy
        self.rightDummy.prev = nodeToInsert

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.cache[key].val = value 
            self.removal(self.cache[key])
        else: 
            self.cache[key] = Node(key, value)

        if(len(self.cache) > self.capacity):
            toRemove = self.leftDummy.next 
            self.removal(toRemove)
            del self.cache[toRemove.key] 

        self.insertion(self.cache[key])














        
