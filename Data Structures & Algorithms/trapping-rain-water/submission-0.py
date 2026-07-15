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
                # l = max(l, height[lidx])
                # res += l - height[lidx]
                
            else:
                if r > height[ridx]:
                    res += r - height[ridx]
                else:
                    r = height[ridx]
                ridx-=1
                # r = max(r, height[ridx])
                # res += r - height[lidx]
                
        return res


# class Solution {
#     public int trap(int[] height) {
#         if(height == null || height.length == 0) return 0;
#         int left = height[0];
#         int lIdx = 0;
#         int n = height.length;
#         int right = height[n-1];
#         int rIdx = n-1;
#         int cnt = 0;
#         while(lIdx <= rIdx){
#             if(left <= right){
#                 if(height[lIdx] < left){
#                     cnt+= left - height[lIdx];
#                 }else{
#                     left = height[lIdx];
#                 }
#                 lIdx++;
#             }else{
#                 if(height[rIdx] < right){
#                     cnt += right - height[rIdx];
#                 }else{
#                     right = height[rIdx];
#                 }
#                 rIdx--;
#             }
#         }
#         return cnt;
#     }
# }

        