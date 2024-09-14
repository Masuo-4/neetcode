from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dct = defaultdict(int)
        count_lst = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count_dct[n] += 1
        for key, v in count_dct.items():
            count_lst[v].append(key)
            
        res = []
        for i in range(len(count_lst) - 1, 0, -1):
            for num in count_lst[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
