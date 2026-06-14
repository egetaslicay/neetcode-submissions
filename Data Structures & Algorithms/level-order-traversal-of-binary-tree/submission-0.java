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
        Queue<TreeNode> workList = new LinkedList<>();
        List<List<Integer>> result = new ArrayList<>();
        workList.add(root); 

        while(!workList.isEmpty()){ 
            List<Integer> levelOfNodes = new ArrayList<>(); 
            
            for(int i = workList.size(); i > 0;  i--){ 
                TreeNode node = workList.poll(); 

                if(node != null){ 
                    levelOfNodes.add(node.val); 
                    workList.add(node.left); 
                    workList.add(node.right); 
                }
            }
                if(levelOfNodes.size() > 0){ 
                    result.add(levelOfNodes); 
                }
            }
        return result;
        }     
    }  
