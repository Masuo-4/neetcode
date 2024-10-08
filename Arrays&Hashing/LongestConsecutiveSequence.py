class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 in num_set:
                continue
            else:
                length = 1
                while (num + length) in num_set:
                    length += 1
                max_length = max(max_length, length)
        return max_length
                