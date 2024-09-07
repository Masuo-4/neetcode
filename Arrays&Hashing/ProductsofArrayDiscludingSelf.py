class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i, num in enumerate(nums):
            if i == 0: continue
            res[i] = res[i - 1] * nums[i - 1]
        
        postfix = 1
        for i, num in reversed(list(enumerate(nums))):
            if i == len(nums) - 1: continue
            res[i + 1] *= postfix
            print(res)
            postfix *= nums[i + 1]
        res[0] *= postfix
        
        return res
