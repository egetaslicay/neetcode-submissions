"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr = head

        hashMap = {} 

        while(curr): 
            hashMap[curr.val] = Node(curr.val, None, None)
            curr = curr.next 

        curr = head 
        tail = dummy 

        while(curr.next): 
            nodeToPut = hashMap[curr.val]
            nodeToPut.next = hashMap[curr.next.val] if curr.next else None 
            nodeToPut.random = hashMap[curr.random.val] if curr.random else None
            tail.next = nodeToPut 
            tail = tail.next 
            curr = curr.next 

        return dummy.next


