class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, num in enumerate(nums):  
            num_dict[target - num] = i
        for i, num in enumerate(nums):
            if num in num_dict:
                if i != num_dict[num]:
                    return [i, num_dict[num]]
        return []
