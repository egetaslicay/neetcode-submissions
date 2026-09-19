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

        diameter = 0 
        order = [root] 

        # completes our BFS 
        for node in order:

            if node.left: order.append(node.left)

            if node.right: order.append(node.right)

        heights = defaultdict(lambda: -1)

        for node in order[::-1]: 

            left = 1 + heights[node.left]
            right = 1 + heights[node.right]

            height = max(left, right)
            heights[node] = height 
            diameter = max(diameter, left + right)


        return diameter 

