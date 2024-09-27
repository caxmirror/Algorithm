"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        oldtocopy = {}
        old = head
        while old != None:
            newnode = Node(old.val)
            oldtocopy[old] = newnode
            old = old.next
        old = head
        while old != None:
            oldtocopy[old].next = oldtocopy[old.next] if old.next!=None else None
            oldtocopy[old].random = oldtocopy[old.random] if old.random!=None else None
            old = old.next
        return oldtocopy[head]


            