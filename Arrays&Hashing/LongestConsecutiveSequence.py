class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            # スタート位置ならば、連続する列の長さを求める。
            if num - 1 not in nums_set:
                search_num = num + 1
                length = 1
                while(search_num in nums_set):
                    if num + 1 in nums_set:
                        length += 1
                        search_num += 1
                    else: break
                # 長さの最大値更新
                longest = max(longest, length)
            # スタート位置じゃないなら無視                  
            else: continue
        return longest
    