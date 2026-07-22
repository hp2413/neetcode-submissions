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
        # temp_res = Node(-1, None, None)
        # res = temp_res
        first = head
        while first:
            newNode = Node(first.val)
            newNode.next = first.next
            first.next = newNode
            first = first.next.next

        first = head
        # res = temp
        while first:  
            if first.random is not None:
                first.next.random = first.random.next
            first = first.next.next


        first = head
        temp_res = first.next
        res = temp_res
        while first:
            first.next = first.next.next
            if res.next is not None:
                res.next = res.next.next
            first = first.next
            res = res.next
        
        return temp_res
                