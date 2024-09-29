from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_by_count = counter.most_common()
        res = []
        for num, count in sorted_by_count:
            if k < 1:
                return res
            else:
                res.append(num)
                k -= 1
        return res         
# valueのみを扱いたいとき、keyをindexとしたlen=len(nums) + 1の空配列を作るのも方法の一つ。
