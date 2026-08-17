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
            kthNode = self.getKth(groupPrev, k)
            if kthNode: 
                groupNext = kthNode.next 

                prev, curr = kthNode.next, groupPrev.next 

                while curr != groupNext: 
                    next = curr.next 
                    curr.next = prev 
                    curr = next 
                    prev = curr

                temp = groupPrev.next 
                groupPrev.next = kthNode
                groupPrev = tmp 
            else: 
                break

        return dummy.next 

    def getKth(self, curr, k): 
        while curr and k > 0: 
            curr = curr.next 
            k -= 1 
        return curr 
