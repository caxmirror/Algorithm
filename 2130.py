# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_best_me:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # redirect the node from mid
        slow, fast = head, head
        pre = None
        nex = slow.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow.next = pre
            pre = slow
            slow = nex
            nex = nex.next
        left, right = pre, slow
        max_twin_sum = 0
        while left != None:
            max_twin_sum = max(max_twin_sum, left.val + right.val)
            left = left.next
            right = right.next
        return max_twin_sum
