from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dct = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in dct:
                if stack and stack[-1] == dct[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
