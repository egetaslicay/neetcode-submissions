# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):
        # base case 
        if not root:
            return 0 

        # global 
        res = float('-inf') 

        def dfs(curr: Optional[TreeNode]): 
            nonlocal res
            if not curr: 
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)

            ## global check 
            res = max(res, curr.val + max(left,0) + max(right, 0))

            return curr.val + max(left, right, 0)

        dfs(root)

        return res 

