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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
    ArrayList<ListNode> nodeList = new ArrayList<>(); 
    ListNode currNode = head; 

    while(currNode != null){ 
        nodeList.add(currNode); 
        currNode = currNode.next;
    }

    if(n == nodeList.size()) {  // base case ig? 
        head = head.next; 
        return head; 
    }

    n = nodeList.size()-n; 
    ListNode curr = head; 

    int i = 0; 
    while(i != n){ 
        if(i == (n-1)){ 
            ListNode nNext = curr.next.next; 
            curr.next = nNext; 
        }
        i++; 
        curr = curr.next; 
    }

    return head; 
    }
}
