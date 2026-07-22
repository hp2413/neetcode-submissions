class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        # [1,2,3,2,2]
        #  0 1 2 3 4
        #.     f 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        
        return fast
        