class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1 , n2 = len(nums1), len(nums2)

        l, r = 0, n1
        while l <= r:
            m1 = l + (r - l) // 2
            m2 = ( (n1 + n2) // 2 ) - m1

            l1 = -math.inf if m1 == 0 else nums1[m1-1]
            l2 = -math.inf if m2 == 0 else nums2[m2-1]
            r1 = math.inf if m1 == n1 else nums1[m1]
            r2 = math.inf if m2 == n2 else nums2[m2]

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


