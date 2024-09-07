from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for spell in s:
            s_count[spell] += 1
            
        for spell in t:
            t_count[spell] += 1

        return t_count == s_count
        