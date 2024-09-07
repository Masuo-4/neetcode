class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, num in enumerate(nums):  
            diff = target - num
            if num in num_dict:
                return [num_dict[num], i]
            else: num_dict[diff] = i

# 自分のことを必要としている数があるかをnum_dictを見て探す。
# あるならnum_dictのkeyがその数がある場所なので、return [相手の場所(num_dict[num]), 自分の場所(i)]
# ないなら自分が求めてる数(target - num)をkeyに、自分の場所(i)をvalueにしてnum_dictに追加する。
