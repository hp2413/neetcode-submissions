class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = math.inf
        pro = 0
        for val in prices:
            b = min(b, val)
            pro = max(pro, val - b)
        
        return pro

# [10,1,5,6,7,1]
# b = min(val, b)
# p = max(p, val - b)