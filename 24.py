# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while head != None and head.next!=None:
            headnext = head.next
            nex = headnext.next
            #swap
            pre.next = headnext
            headnext.next = head
            head.next = nex
            pre = head
            head = nex
            
        return dummy.next