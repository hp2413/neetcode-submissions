class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
            
        return res
        # [0,  0, 0, 2, 1, 0, 0]
        # [30,38,30,36,35,40,28]
        # 40,35,  
            
        