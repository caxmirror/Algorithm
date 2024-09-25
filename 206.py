# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        cur = ListNode()
        nex = ListNode()
        pre = ListNode()

        cur = head.next
        nex = cur.next
        cur.next = head
        head.next = None
        while nex != None:
            pre = cur
            cur = nex
            nex = nex.next
            cur.next = pre
        return cur
            
            

            
