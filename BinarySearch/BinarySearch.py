class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r= 0, len(nums) - 1
         
        while l <= r:
            # overflowを防ぐ
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
        return -1
