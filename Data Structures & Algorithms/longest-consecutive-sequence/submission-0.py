class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        cnt = 0
        for num in hs:
            if (num - 1) not in hs:
                curr = num - 1
                cnt = 0
                while (curr + 1) in hs:
                    curr += 1
                    cnt += 1
                res = max(cnt, res)
        return res
        