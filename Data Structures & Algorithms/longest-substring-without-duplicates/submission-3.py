class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        #  0123456

        # z - 1
        # x - 1
        # y - 2
        l = 0
        res = 0
        hm = {}

        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
            hm[s[r]] = r
            res = max(res , r - l + 1)
        
        return res
