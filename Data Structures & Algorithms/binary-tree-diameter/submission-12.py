# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 

        order = []
        queue = deque([root]) 

        while queue: 
            node = queue.popleft() 
            order.append(node)

            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)


        heights = {} 
        res = 0 

        for node in order[::-1]: 
          
            left = 1 + heights.get(node.left, -1)
            right = 1 + heights.get(node.right, -1)
              
            res = max(res, left + right)
            
            heights[node] = max(left, right)

        return res 




