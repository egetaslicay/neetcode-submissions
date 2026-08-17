# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = [] 
        
        while(head): 
            nodeList.append(head)
            head = head.next

        left = 0 
        right = len(nodeList)-1


        while(left <= right):  
            nodeList[left].next = nodeList[right]
            nodeList[right].next = nodeList[left+1]
            left += 1
            right -= 1