# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [] 

        queue.append(root)

        while(queue):
            numNodes = len(queue)
            level = [] 

            for i in range(numNodes): 
                curr = queue.popleft() 
                temp.append(curr)

                if(curr.left):
                    queue.append(curr.left)

                if(curr.right): 
                    queue.append(curr.right)

            res.append(temp)

        return res 

