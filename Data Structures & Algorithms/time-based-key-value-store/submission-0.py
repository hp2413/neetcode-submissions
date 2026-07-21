class TimeMap:

    def __init__(self):
        self.keyStore = {} # key : list [val, time]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res, val = "", self.keyStore.get(key, [])
        l = 0
        r = len(val) - 1 
        while l <=r :
            m = l + ( r - l ) // 2
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m + 1 
            else:
                r = m - 1
        return res
