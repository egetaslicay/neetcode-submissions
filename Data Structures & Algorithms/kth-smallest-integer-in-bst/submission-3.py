# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: 
            return None 
        
        valList = [] 
        
        def dfs(curr: Optional[TreeNode]): 
            if(not curr): 
                return 
                
            valList.append(curr.val)

            dfs(curr.left)
            dfs(curr.right)

        dfs(root)      
        valList.sort()

        return valList[k-1]