# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # do to mid 
        # split 
        # revert the second half 
        # res = ListNode(-1)
        # res.next = head
        first = head
        second = head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        
        mid = first.next
        first.next = None
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 

        

        