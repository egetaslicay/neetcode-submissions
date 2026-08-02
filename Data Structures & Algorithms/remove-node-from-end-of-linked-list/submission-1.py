# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() 
        dummy.next = head

        curr = dummy 
        length = 0

        while(curr.next): 
            length+= 1
            curr = curr.next 

        beforeRemoveNode = dummy 
        distForwards = 0

        while(distForwards != length - n): 
            beforeRemoveNode = beforeRemoveNode.next
            distForwards += 1 

        
        if(beforeRemoveNode.next): 
            newNext = beforeRemoveNode.next.next
            beforeRemoveNode.next = newNext 

        return dummy.next
        


        