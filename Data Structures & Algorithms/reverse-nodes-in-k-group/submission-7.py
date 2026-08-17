# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy 

        while(True): 
            kthNode = self.getKthNode(groupPrev, k)
    
            if kthNode:
                prev = kthNode.next  
                curr = groupPrev.next 

                while(curr): 
                    tmp = curr.next 
                    curr.next = prev 
                    prev = curr
                    curr = tmp 

                tmp = groupPrev.next 
                groupPrev.next = kthNode 
                groupPrev = tmp

            else: 
                break 

        return dummy.next




    def getKthNode(self, curr, k): 
        while curr and k > 0: 
            curr = curr.next 
            k -= 1

        return curr