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

        diameter = float('-inf')

        def height(node: Optional[TreeNode]) -> int: 
            nonlocal diameter 
            if not node: 
                return -1 

            left = 1 + height(node.left)
            right = 1 + height(node.right)

            res = max(left, right)
            diameter = max(diameter, left + right) 

            return res 

        height(root)
        return diameter