class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        t_count = collections.Counter(t)
        s_count = Counter()
        have, need = 0, len(t_count)
        res, resLen = [-1, -1], float("inf") # res = [l, r]
        l = 0

        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1

            if c in t_count and s_count[c] == t_count[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                s_count[s[l]] -= 1

                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
        