class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l , r = 0, n-1
        while (l <= r):
            m = l + ((r - l) // 2)
            if (m == 0 or (nums[m-1] > nums[m])) and ( m == n-1 or nums[m] < nums[m+1]):
                return nums[m]
            elif nums[m] < nums[r]:
               r = m - 1
            else:
                l = m + 1

        return nums[r] 


# class Solution {
#     public int findMin(int[] nums) {
#         int l = 0;
#         int r = nums.length-1;
#         while(l<=r){
#             int m = l + ( r - l )/ 2;
#             if((m == nums.length-1 || nums[m] < nums[m+1]) && ( m == 0 || nums[m] < nums[m-1])){
#                 return nums[m];
#             }
#             if(nums[m] < nums[r]){
#                 r = m - 1;
#             }else{
#                 l = m + 1;
#             }
#         }
#         return nums[r];
#     }
# }