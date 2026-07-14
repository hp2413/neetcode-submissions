class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 0:
            return []
        res = [0] * n
        mul = nums[0]
        for i in range(1, n):
            res[i] = mul
            mul = mul * nums[i]
        
        mul = nums[n-1]
        for i in range(2, n):
            res[n-i] = res[n-i] * mul
            mul = mul * nums[n-i]
        res[0] = mul

        return res

        