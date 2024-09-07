class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        spell_dict_s = dict()
        for spell in s:
            if spell in spell_dict_s:
                spell_dict_s[spell] += 1
            else:
                spell_dict_s[spell] = 1
                
        spell_dict_t = dict()
        for spell in t:
            if spell in spell_dict_t:
                spell_dict_t[spell] += 1
            else:
                spell_dict_t[spell] = 1
        
        return spell_dict_t == spell_dict_s
        
        