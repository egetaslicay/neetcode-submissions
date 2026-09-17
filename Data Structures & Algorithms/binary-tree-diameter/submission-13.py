# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 
    

        def dp(node: Optional[TreeNode]): 
            nonlocal res

            if not node: 
                return -1 

            left = 1+dp(node.left)
            right = 1+dp(node.right)
            
            res = max(res, left + right)
            return max(left, right)
        
        dp(root)
        return res 