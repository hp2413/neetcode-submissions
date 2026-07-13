# [3,4,5,6], target = 7

# 6:0
# 5:1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0:
            return []
        mp = dict()
        for i in range(len(nums)):
            if nums[i] in mp:
                return [mp[nums[i]], i]
            else:
                mp[target-nums[i]] = i
        return []


        