# time: n
# space: n
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head) # 这个写法没问题吧?
        cur = dummy
        
        while cur and cur.next:
            tmp = cur
            while tmp and tmp.next and tmp.next.val == val:
                tmp = tmp.next
            cur.next = tmp.next
            cur = cur.next
        return dummy.next