# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root 

        while(True): 
            if(root.val < p.val and root.val < q.val): 
                lca = root
                root = root.right
            elif(root.val > p.val and root.val > q.val): 
                lca = root
                root = root.left
            else: 
                return lca 

        return None 

        