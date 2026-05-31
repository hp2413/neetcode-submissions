class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while(l < r):
            val = (r - l) * min(heights[r], heights[l])
            res = max(res, val)
            if(heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        return res
#. l
# [1,7,2,5,4,7,3,6]
#                r
#        