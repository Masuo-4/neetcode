from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s1_len = len(s1)
        s2_len = len(s2)
        window_counter = Counter()

        for i in range(s2_len):
            window_counter[s2[i]] += 1

            if i >= s1_len:
                if s2[i - s1_len] == 1:
                    del window_counter[s2[i - s1_len]]
                else: window_counter[s2[i - s1_len]] -= 1
            if s1_count == window_counter:
                return True
        return False
