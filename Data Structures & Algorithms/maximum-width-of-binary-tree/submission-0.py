# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque() 
        maxWidth = 1
        depth = 0 

        if not root: 
            return 0 

        queue.append((root,0))

        while queue: 
            numPops = len(queue)
            leftmost = queue[0][1]
            rightmost = queue[-1][1]

            maxWidth = max(maxWidth, rightmost - leftmost + 1)
            
            for i in range(numPops): 
                popped = queue.popleft() 
                seat = popped[1]
                node = popped[0]

                if node.left: queue.append((node.left, 2 * seat))
                if node.right: queue.append((node.right, 2 * seat + 1))


        return maxWidth
                