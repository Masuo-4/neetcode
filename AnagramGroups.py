from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = dict()
        for word in strs:
            count_dict = defaultdict(int)
            for s in word:
                count_dict[s] += 1
            count_dict = sorted(count_dict.items())
            # listやdictは辞書のキーには使えない
            count_dict_tuple = tuple(count_dict)
            if count_dict_tuple in group_dict:
                group_dict[count_dict_tuple].append(word)
            else:
                group_dict[count_dict_tuple] = [word]
        
        return list(group_dict.values())
