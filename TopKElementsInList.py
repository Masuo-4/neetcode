from collections import defaultdict
# バケットソートを使う
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]      
        for num in nums:
            count[num] += 1
        for num, count in count.items():
            freq[count].append(num)
        res = []
        for num in reversed(freq):
            # リストの連結
            res.extend(num)
            if len(res) == k:
                return res
            