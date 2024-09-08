class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for i in range(len(s)):
            if s[i].isalnum():
                # new_s += s[i].lower()よりも速い
                new_s.append(s[i].lower())
        new_s = "".join(new_s)
        # reversedだけではreversedオブジェクトというイテレータが返されてしまう。
        return new_s == new_s[::-1]
