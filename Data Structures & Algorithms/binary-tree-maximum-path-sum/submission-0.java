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
    public int maxSum = Integer.MIN_VALUE; 
    public int maxPathSum(TreeNode root) {
        maxGain(root); 
        return maxSum;
    }
    public int maxGain(TreeNode root){ 
        if(root == null){
            return 0; 
        }

        int maxGainLeft = Math.max(maxGain(root.left), 0); 
        int maxGainRight = Math.max(maxGain(root.right), 0); 

        int newPathSum = root.val + maxGainLeft + maxGainRight; 

        if(newPathSum > maxSum){ 
            maxSum = newPathSum; 
        }

        return root.val + Math.max(maxGainLeft, maxGainRight); 
    }

}
