# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        reverse = False 
        res = [] 
        queue = deque() 

        if not root: 
            return res  
        
        queue.append(root) 

        while queue: 
            numPops = len(queue)
            level = [] 

            for i in range(numPops): 
                popped = queue.popleft() 

                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)

                level.append(popped.val)

            if reverse: 
                res.append(level[::-1])
            else: 
                res.append(level)

            reverse = not reverse 

        return res 



