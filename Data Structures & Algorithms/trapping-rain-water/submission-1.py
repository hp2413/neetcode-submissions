class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        n = len(height)
        lidx = 0
        l = height[lidx]
        res = 0
        ridx = n-1 
        r = height[ridx]
        while lidx <= ridx:
            if l <= r:
                if l > height[lidx]:
                    res += l - height[lidx]
                else:
                    l = height[lidx]
                lidx+=1
            else:
                if r > height[ridx]:
                    res += r - height[ridx]
                else:
                    r = height[ridx]
                ridx-=1
        return res

   