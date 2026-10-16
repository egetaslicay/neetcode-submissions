# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res =[] 

        if not root:
            return res 

        queue.append(root)

        while queue: 
            numToPop = len(queue)
            level = [] 

            for i in range(numToPop):
                popped = queue.popleft()
                level.append(popped.val)
                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)

            res.append(level)

        return res 


