# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1!=None and l2!=None:
            total = l1.val + l2.val + carry
            carry = total // 10
            total = total % 10
            head.next = ListNode(total)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        while l1 == None and l2!=None:
            total = l2.val + carry
            carry = total // 10
            total = total % 10
            head.next = ListNode(total)
            head = head.next
            l2 = l2.next
        while l2 == None and l1!=None: 
            total = l1.val + carry
            carry = total // 10
            total = total % 10
            head.next = ListNode(total)
            head = head.next
            l1 = l1.next
        if carry != 0:
            head.next = ListNode(1)
        return dummy.next



