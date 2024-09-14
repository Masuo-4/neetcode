from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = defaultdict(int)
        for i, n in enumerate(nums):
            if n in dct:
                return [dct[n], i]
            else:
                dct[target - n] = i