class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = "".join(res + str(len(s)) + "#" + s)
        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        i = 0
        res = []
        while i < len(s):
            if s[i] != "#":
                num = "".join(num + s[i])
            else:
                length = int(num)
                num = ""
                word = s[i + 1: i + 1 + length]
                res.append(word)
                i += length
            i += 1
        return res
