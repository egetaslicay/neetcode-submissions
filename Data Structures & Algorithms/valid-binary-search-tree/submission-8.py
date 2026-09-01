# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 

        def dfs(self, curr: Optional[TreeNode], minBound: float, maxBound: float): 
            if not curr: 
                return True

            if curr > minBound and curr < maxBound: 
                return dfs(curr.left, minBound, curr.val) and dfs(curr.right, curr.val, maxBound) 

            else: 
                return False 


        left = dfs(root.left, float('inf'), root.val)
        right = dfs(root.right, root.val, float('inf'))


        if(left and right): 
            return True
        else: 
            return False





