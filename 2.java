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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        int sum = 0;
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        while (l1!=null && l2!=null){
            sum = l1.val + l2.val + carry;
            ListNode listnode = new ListNode();
            listnode.val = sum % 10;
            carry = sum/10;
            cur.next = listnode;
            cur = cur.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        if(l1 == null){if(carry==0){cur.next = l2;}
        else{
            while(l2!=null && carry != 0){
                sum = carry + l2.val;
                ListNode listnode = new ListNode();
                listnode.val = sum % 10;
                carry = sum/10;
                cur.next = listnode;
                cur = cur.next;
                l2 = l2.next;
            }
            if(carry != 0){
                ListNode listnode = new ListNode(1);
                cur.next = listnode;
            }
            else if(l2 != null){
                cur.next = l2;
            }
        }
        }

        else{
            if(carry==0){cur.next = l1;}
            else{
            while(l1!=null && carry != 0){
                sum = carry + l1.val;
                System.out.println(sum);
                ListNode listnode = new ListNode();
                listnode.val = sum % 10;
                carry = sum/10;
                cur.next = listnode;
                cur = cur.next;
                l1 = l1.next;
            }
            if(carry != 0){
                ListNode listnode = new ListNode(1);
                cur.next = listnode;
            }
            else if(l1 != null){
                cur.next = l1;
            }
        }
        }
        return dummy.next;
    }
}