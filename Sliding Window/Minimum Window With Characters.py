from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        have, need = 0, len(t)
        count_t,  window_count = Counter(t), Counter()
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            window_count[s[r]] += 1
            if s[r] in count_t and window_count[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window_count[s[l]] -= 1 
                if s[l] in count_t and window_count[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l: r + 1] if resLen != float("infinity") else ""
