class Node:
    def __init__(self, val: int, key: int): 
        self.val = val
        self.key = key 
        self.next = None 
        self.prev = None 




class LRUCache:
    def __init__(self, capacity: int):
        self.keyToNode = {} 
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.capacity = capacity
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key not in self.keyToNode: 
            return -1 

        currNode = self.keyToNode[key]
        self.remove(currNode)
        self.insert(currNode)
        return currNode.val

    def put(self, key: int, value: int) -> None:
        if len(self.keyToNode) >= self.capacity and key not in self.keyToNode:
            nodeToRemove = self.right.prev 
            keyToRemove = nodeToRemove.key
            del self.keyToNode[keyToRemove]
            self.remove(nodeToRemove)

        newNode = Node(value, key)
        # remove the node associated with this key if there is one 
        if key in self.keyToNode: 
            self.remove(self.keyToNode[key])

        # insert the node and update the value 
        self.insert(newNode)
        self.keyToNode[key] = newNode 

    def remove(self, node) -> None:
        next = node.next 
        prev = node.prev 
        prev.next = next 
        next.prev = prev 
        node.next = None # these arent strictly needed but oh well
        node.prev = None # these arent strictly needed but oh well

    def insert(self, node) -> None: # whenever we insert always insert at the left
        prevMostRecent = self.left.next 
        self.left.next = node 
        node.prev = self.left 
        node.next = prevMostRecent
        prevMostRecent.prev = node 


        
