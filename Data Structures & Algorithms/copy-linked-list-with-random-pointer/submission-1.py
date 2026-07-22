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
        if head is None:
            return head
        
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random is not None:
                curr.next.random = curr.random.next 
            curr = curr.next.next
        
        curr = head
        res = curr.next
        temp = curr.next
        while curr:
            curr.next = curr.next.next
            if temp.next is not None:
                temp.next = temp.next.next
            curr = curr.next
            temp = temp.next
        
        return res
            
        