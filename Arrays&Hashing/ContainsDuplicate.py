class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict()
        for i, num in enumerate(nums):
            if num in num_dict:
                return True
            else:
                num_dict[num] = num
        
        return False
