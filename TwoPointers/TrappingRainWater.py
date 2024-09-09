class Solution:
    def trap(self, height: List[int]) -> int:
        rain_sum = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        rain_sum = 0
        while l < r :
            if l_max <= r_max:
                l += 1
                l_max = max(height[l], l_max)
                rain_sum += l_max - height[l]
            elif r_max < l_max:
                r -= 1
                r_max = max(height[r], r_max)
                rain_sum += r_max - height[r]
        
        return rain_sum
            