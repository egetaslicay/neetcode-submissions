# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode() 
        tail = dummy
        myHeap = [] 

        for i, node in enumerate(lists): 
            if node:
                heapq.heappush(myHeap, (node.val, i, node))

        while(myHeap): 
            val, i, node = heapq.heappop(myHeap)
            tail.next = node 
            tail = tail.next 
            if node.next: 
                heapq.heappush(myHeap, (node.next.val, i, node.next))

        return dummy.next 

        



