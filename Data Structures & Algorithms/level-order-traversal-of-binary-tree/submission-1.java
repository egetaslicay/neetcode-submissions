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
    public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>(); 
    Queue<TreeNode> workList = new ArrayDeque<>();
        
    if(root == null){
        return result;
    }
    workList.add(root); 

    while(!workList.isEmpty()) { 
        List<Integer> level = new ArrayList<>(); 
        int qLength = workList.size(); 
        for(int i = 0; i < qLength; i++) {
        TreeNode currNode = workList.poll();    
        if(currNode.left != null) { workList.add(currNode.left); }
        if(currNode.right != null) { workList.add(currNode.right); } 
        level.add(currNode.val);
        }
        result.add(level); 

    }   

    return result;

        }     
    }  
