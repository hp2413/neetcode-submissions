class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        A, B = nums1, nums2
        n1 , n2 = len(A), len(B)

        l, r = 0, n1
        while l <= r:
            m1 = l + (r - l) // 2
            m2 = ( (n1 + n2) // 2 ) - m1

            l1 = -math.inf if m1 == 0 else A[m1-1]
            l2 = -math.inf if m2 == 0 else B[m2-1]
            r1 = math.inf if m1 == n1 else A[m1]
            r2 = math.inf if m2 == n2 else B[m2]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2)%2 == 0:
                    return (max(l1, l2)+min(r1,r2)) / 2
                else:
                    return min(r1, r2)
            elif l1 > r2 :
                r = m1 - 1
            else:
                l = m1 + 1
        
        return -1



# class Solution {
#     public double findMedianSortedArrays(int[] nums1, int[] nums2) {
#         // if(nums1 == null && nums2 == null) return;
#         int n1 = nums1.length;
#         int n2 = nums2.length;
#         if(n1 > n2) return findMedianSortedArrays(nums2, nums1);
#         int l = 0;
#         int r = n1;
#         while(l <= r){
#             int m1 = l + (r - l)/2;
#             int m2 = (n1 + n2)/2 - m1;
#             double l1 = m1 == 0 ? Integer.MIN_VALUE : nums1[m1-1];
#             double l2 = m2 == 0 ? Integer.MIN_VALUE : nums2[m2-1];
#             double r1 = m1 == n1 ? Integer.MAX_VALUE : nums1[m1];
#             double r2 = m2 == n2 ? Integer.MAX_VALUE : nums2[m2];
#             if(l1 <= r2 && l2 <= r1){
#                 if((n1+n2)%2 == 0){
#                     return (Math.max(l1, l2)+Math.min(r1, r2))/2;
#                 }else{
#                     return Math.min(r1, r2);
#                 }
#             }else if( l1 > r2){
#                 r = m1 - 1;
#             }else{
#                 l = m1 + 1;
#             }
#         }
#         return -1;
#     }
# }