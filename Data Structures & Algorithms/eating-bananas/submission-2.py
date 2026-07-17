class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,4,3,2]
        #  9h
        # 1,2,3,4
        l, r = 1, max(piles)
        res = r
        while l < r:
            m = l + (r - l) // 2
            if self.getHours(piles, m) <= h:
                res = m
                r = m
            else:
                l = m + 1
        return res
    
    def getHours(self, piles: List[int], m: int):
        cnt = 0
        for p in piles:
            cnt += p // m
            if p % m != 0:
                cnt += 1
        return cnt
