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

        for i, node in enumerate(lists): 
            if node: 
                heapq.heappush(myHeap, (node.val,i, node)) 


        while(myHeap): 
            nodeToAdd = heapq.heappop(myHeap) 
            tail.next = nodeToAdd 
            tail = tail.next 
            heapq.heappush(myHeap, (nodeToAdd.val, nodeToAdd)) 


        return dummy.next 

