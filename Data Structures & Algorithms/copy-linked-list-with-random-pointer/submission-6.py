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
        if not head: 
            return None 

        dummy = Node(0)
        curr = head

        hashMap = {} 

        while(curr): 
            hashMap[curr] = Node(curr.val, None, None)
            curr = curr.next 

        curr = head 
        tail = dummy 

        while(curr): 
            nodeToPut = hashMap[curr.val]
            nodeToPut.next = hashMap[curr.next] if curr.next in hashMap else None 
            nodeToPut.random = hashMap[curr.random] if curr.random in hashMap else None
            tail.next = nodeToPut 
            tail = tail.next 
            curr = curr.next 

        return dummy.next


