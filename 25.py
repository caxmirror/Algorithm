# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        if k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        kcount = k

        while head != None:
            # reach end of kcount
            while head != None and kcount>1: 
                kcount -= 1
                head = head.next
                if head == None:
                    return dummy.next
            nex = head.next
            tail = pre.next #

            l = pre
            ltail = pre.next
            r = head
            # reverse link list
            while l != r: 
                tailnext = ltail.next
                ltail.next = l
                l = ltail
                ltail = tailnext
            tail.next = nex
            pre.next = head

            pre = tail
            head = nex
            kcount = k
        return dummy.next
                





            
