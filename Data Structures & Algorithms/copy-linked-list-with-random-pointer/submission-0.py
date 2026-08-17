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
        dummy = Node()
        curr = head

        hashMap = {} 

        while(curr.next): 
            hashMap[curr.val] = ListNode(curr.val, None, None)
            curr = curr.next 

        curr = head 
        tail = dummy 

        while(curr.next): 
            nodeToPut = hashMap[curr.val]
            nodeToPut.next = hashMap[curr.next.val] if curr.next else None 
            nodeToPut.random = hashMap[curr.random.val] if curr.random else None

        return dummy.next


