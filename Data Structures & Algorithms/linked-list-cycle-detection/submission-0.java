/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        int index = 0; 
        ListNode currNode = head; 
        HashMap<ListNode, Integer> nodeMap = new HashMap<>(); 

        while(currNode != null){ 
            if(!nodeMap.containsKey(currNode)){ 
                nodeMap.put(currNode, index); 
            } else { 
                return true; 
            }

            currNode = currNode.next; 
            index++; 

        }
        return false; 
    }
}
