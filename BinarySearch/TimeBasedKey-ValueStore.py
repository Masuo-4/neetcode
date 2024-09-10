class TimeMap:

    def __init__(self):
        self.dct = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = []
        self.dct[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ""
        time_value_lst = self.dct[key]
        l, r = 0, len(time_value_lst) - 1
        res = "" 
        while l <= r:
            m = l + (r - l) //2
            if timestamp >= time_value_lst[m][0]:
                res = time_value_lst[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
            
        
        
  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)