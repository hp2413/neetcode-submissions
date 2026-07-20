# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currOne = list1
        currTwo = list2
        res = ListNode(-1)
        ans = res
        while currOne and currTwo:
            if currOne.val <= currTwo.val:
                res.next = ListNode(currOne.val)
                currOne = currOne.next
            else:
                res.next = ListNode(currTwo.val)
                currTwo = currTwo.next
            res = res.next
        
        while currOne:
            res.next = ListNode(currOne.val)
            currOne = currOne.next
            res = res.next
        
        while currTwo:
            res.next = ListNode(currTwo.val)
            currTwo = currTwo.next
            res = res.next
        
        return ans.next
            

        