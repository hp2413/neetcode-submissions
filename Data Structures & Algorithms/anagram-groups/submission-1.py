class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for st in strs:
            key = self.getKey(st)
            if key not in hm:
                hm[key] = []
            
            hm[key].append(st)
        
        res = []
        for k in hm.keys():
            res.append(hm[k])

        return res

    def getKey(self, strs: str) -> str:
        res = [0] * 26
        for s in strs:
            res[ord(s)-ord('a')] += 1
        
        res_str = ""
        for v in res:
            res_str = res_str + str(v) + "#"
        return res_str
        