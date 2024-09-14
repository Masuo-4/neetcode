class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = self.make_prefix(nums)
        print(pref)
        postf = self.make_prefix(nums[::-1])[::-1]
        print(postf)
        res = []
        for i in range(len(nums)):
            res.append(pref[i] * postf[i])
        return res
    
    def make_prefix(self, nums):
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        return res
