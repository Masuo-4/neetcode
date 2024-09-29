class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = collections.Counter(s1)
        s1_len, s2_len = len(s1), len(s2)
        s2_count = collections.Counter()
        for i in range(s2_len):
            s2_count[s2[i]] += 1
            if i >= s1_len:
                if s2_count[s2[i - s1_len]] == 1:
                    del s2_count[s2[i - s1_len]]
                else:
                    s2_count[s2[i - s1_len]] -= 1
            if s1_count == s2_count:
                return True
        return False
