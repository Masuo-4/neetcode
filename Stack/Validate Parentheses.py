from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dct = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c not in dct:
                stack.append(c)
                continue
            if not stack or stack[-1] != dct[c]:
                return False
            stack.pop()
        return not stack 
