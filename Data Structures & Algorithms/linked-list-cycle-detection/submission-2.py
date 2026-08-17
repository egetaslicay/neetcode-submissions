# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head): 
            return False
    
        fast = head 
        slow = head 
        count = 1 


        while(fast): 
            fast = fast.next
            if(count % 2): 
                slow = slow.next 
            
            if(fast == slow): 
                return True

            count += 1 

        return False