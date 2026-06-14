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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode curr1 = list1;
        ListNode curr2 = list2;

        ListNode newListHead = null; 
        ListNode newListTail = null; 
        boolean firstInsertion = true; 

        while(curr1 != null || curr2 != null){ 
            if(curr1 == null){ 
                if(firstInsertion == true){ 
                    newListHead = curr2;
                    newListTail = curr2; 
                    firstInsertion = false;
                } else { 
                    newListTail.next = curr2;
                    newListTail = newListTail.next;
                }
                curr2 = curr2.next;
                continue;
            }

            if(curr2 == null){ 
               if(firstInsertion == true){ 
                    newListHead = curr1;
                    newListTail = curr1; 
                    firstInsertion = false;
                } else { 
                    newListTail.next = curr1; 
                    newListTail = newListTail.next;
                }
                curr1 = curr1.next;
                continue;
            }



            if(curr1.val <= curr2.val){ 
                if(firstInsertion == true){ 
                    newListHead = curr1;
                    newListTail = curr1; 
                    firstInsertion = false;
                } else { 
                    newListTail.next = curr1; 
                    newListTail = newListTail.next;
                }
                curr1 = curr1.next;
            } else { 
                if(firstInsertion == true){ 
                    newListHead = curr2;
                    newListTail = curr2; 
                    firstInsertion = false;
                } else { 
                    newListTail.next = curr2;
                    newListTail = newListTail.next;
                }
                curr2 = curr2.next;
            }

        }
        return newListHead; 
    }
}