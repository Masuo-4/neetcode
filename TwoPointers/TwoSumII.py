class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while(l < r):
            num_sum = numbers[l] + numbers[r]

            if num_sum == target:
                return [l + 1, r + 1]

            elif num_sum < target:
                l += 1

            elif num_sum > target:
                r -= 1
