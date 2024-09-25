# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        nex = head.next
        cur = head
        pre = None
        if head.next == None:
            return True
        while fast != None and fast.next != None: 
            fast = fast.next.next
            cur.next = pre
            pre = cur
            cur = nex
            nex = nex.next
        if fast == None: #odd
            left = pre
            right = cur 
        else: 
            left = pre
            right = cur.next 
        while left.val == right.val:
            if left.next == None and right.next==None:
                return True
            elif left.next == None or right.next==None:
                return False
            else:
                left = left.next
                right = right.next
        return False
