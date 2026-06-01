class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] in hm:
                l = max(hm[s[i]]+1, l)
            hm[s[i]] = i
            res = max(res, i - l + 1)
        
        return res


# "zxyzxyz"
#  z = 0
#  x = 1
#  y = 2

# 
        