class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # mul = 6
        # [1,1,2,8]
        n = len(nums)
        res = [0] * n
        mul = nums[0]
        for i in range(1, n):
            res[i] = mul
            mul = (mul * nums[i])
        
        mul = nums[n-1]
        for i in range(2, n):
            res[n-i] = res[n-i] * mul
            mul = mul * nums[n-i]

        res[0] = mul
        return res
            
            
        