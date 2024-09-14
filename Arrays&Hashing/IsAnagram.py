from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in range(len(s)):
            s_count[s[i]] += 1
            
        for i in range(len(t)):
            t_count[t[i]] += 1
        return s_count == t_count
        