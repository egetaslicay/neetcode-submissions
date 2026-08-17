# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    count = 0 

    def goodNodes(self, root: TreeNode) -> int:
        if(not root): 
            return self.count 

        self.count = 1 

        def dfs(curr: TreeNode, maxSF: int): 
            if(not curr):
                return

            if(curr.val >= maxSF): 
                self.count += 1 
                if(curr.left): 
                    dfs(curr.left, curr.val)
                if(curr.right): 
                    dfs(curr.right, curr.val)
            else: 
                if(curr.left): 
                    dfs(curr.left, maxSF)
                if(curr.right): 
                    dfs(curr.right, maxSF)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return self.count