# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root): 
            return True
        
        def dfs(curr):

            if(not curr): 
                return 0 
            
            left = dfs(curr) + 1 
            right = dfs(curr) + 1

            height = max(left, right)

            return height

        leftHeight = dfs(curr.left)
        rightHeight = dfs(curr.right)

        if(abs(leftHeight - rightHeight) > 1): 
            return False

        return True