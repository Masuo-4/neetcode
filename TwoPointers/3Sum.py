class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while (l < r):
                cur_sum = nums[l] + nums[r]
                if cur_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # l と r の重複チェック
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
                elif cur_sum < target:
                    l += 1

                elif cur_sum > target:
                    r -= 1
            i += 1
        return res
