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
    public int kthSmallest(TreeNode root, int k) {
        if(root == null){
            return -1; 
        }
        List<TreeNode> nodesInOrder = new ArrayList<>(); 

        inOrderHelper(root, nodesInOrder);

        k = k-1; 

        return nodesInOrder.get(k).val;
    }

    public void inOrderHelper(TreeNode node, List<TreeNode> list) {
    if (node == null) {
        return;
    }

    inOrderHelper(node.left, list);
    list.add(node);
    inOrderHelper(node.right, list);
    }



}
