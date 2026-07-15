class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        maxA = 0
        while(l < r):
            minH = min(heights[l], heights[r])
            maxA = max(maxA, minH*(r-l))
            if minH == heights[l]:
                l+=1
            else:
                r-=1
        
        return maxA
        