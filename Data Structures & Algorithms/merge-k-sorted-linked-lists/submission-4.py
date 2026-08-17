# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy

        myHeap = [] 

        for node in lists: 
            heapq.heappush(myHeap, node)


        while(myHeap): 
            nodeToAdd = heapq.heappop(myHeap) 
            tail.next = nodeToAdd 
            tail = tail.next 
            heapq.heappush(nodeToAdd.next)


        return dummy.next 

