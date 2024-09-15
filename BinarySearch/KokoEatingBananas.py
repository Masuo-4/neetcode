class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile
        res = max_pile
        while l <= r:
            time = 0
            m = l + (r - l) // 2
            for pile in piles:
                time += math.ceil(float(pile)/m)
            if time > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res
