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
    public ListNode mergeKLists(ListNode[] lists) {
    ListNode dummy = new ListNode(); 
    ListNode tail = dummy;
    PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a,b)-> a.val - b.val); 

    for(ListNode l : lists){ 
        if(l != null){
        minHeap.add(l); 
        }
    }

    while(!minHeap.isEmpty()){
        ListNode popped = minHeap.poll(); 
        tail.next = popped;
        if(popped.next != null){
            minHeap.add(popped.next); 
        }
        tail = tail.next; 
    }

    return dummy.next; 

    }
}
