# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # revl1 = self.reverseList(l1)
        # revl2 = self.reverseList(l2)
        res = ListNode(-1)
        curr = res
        c = 0
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + c
            c = sum//10
            val =  sum%10 
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        
        
        return res.next
            


    def reverseList(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l1
        prev = None
        curr = l1
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev 
