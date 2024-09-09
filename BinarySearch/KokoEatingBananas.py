class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            time = 0
            m = l + (r - l) // 2
            for num in piles:
                time += math.ceil(float(num) / m)
            if time <= h:
                res = m
                r = m - 1
            elif time > h:
                l = m + 1 
        return res
