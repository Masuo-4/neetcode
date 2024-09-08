class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            # スタート位置ならば、連続する列の長さを求める。
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                        length += 1
                longest = max(length, longest)
        return longest
    