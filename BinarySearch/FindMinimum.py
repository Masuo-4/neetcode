class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= nums[r]:
                r = m   # 最小値が左側またはmにある
            else:
                l = m + 1  # 最小値が右側にある

        return nums[l]  # ループが終了したら、lが最小値を指している
