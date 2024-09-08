class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = s + str(len(word)) + "#" + word 
        return s

    def decode(self, s: str) -> List[str]:
        num_str = ""
        res = []
        j = 0
        while j < len(s):
            if s[j] == "#":
                # "#"の次から、文字数分切り取ってリストに追加
                res.append(s[j + 1: j + 1 + int(num_str)])
                j += int(num_str)
                num_str = ""
                
            else:
                num_str += s[j]
            j += 1
        
        return res
        