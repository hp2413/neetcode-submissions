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

# class Solution {
#     public int minEatingSpeed(int[] piles, int h) {
#         if(piles == null || piles.length == 0) return 0;
#         int r = Integer.MIN_VALUE;
#         for(int n : piles){
#             r = Math.max(n, r);
#         }
#         int l = 1;
#         int res = piles[0];
#         while(l < r){
#             int m = l + (r-l)/2;
#             int getH = getHours(piles, m);
#             if(getH <= h){
#                 r = m;
#             }else{
#                 l = m + 1;
#             }
#         }
#         return r;
#     }
#     private int getHours(int [] piles, int m){
#         int cnt = 0;
#         for(int p : piles){
#             cnt += p/m;
#             if(p % m != 0){
#                 cnt++;
#             }
#         }
#         return cnt;
#     }
# }