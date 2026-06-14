/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){
            return null;
        }
          if(containsNodeInSubtree(root, p) && containsNodeInSubtree(root, q)){
     
        TreeNode left = lowestCommonAncestor(root.left, p, q); 
        TreeNode right = lowestCommonAncestor(root.right, p, q); 

        if(left == null && right == null){
            return root;
        }

        if(left != null){
            return left; 
        } else {
            return right;
        }
          }

        return null;
    }


    public boolean containsNodeInSubtree(TreeNode root, TreeNode numToSearchFor){
       if(numToSearchFor == null){
        return true;
       }
       if(root == null){
        return false; 
       }

       if(root.val == numToSearchFor.val){
        return true; 
       } 

       return containsNodeInSubtree(root.left, numToSearchFor) || containsNodeInSubtree(root.right, numToSearchFor); 
    }
}
