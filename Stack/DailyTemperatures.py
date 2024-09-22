class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, i
        lst = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stack_i = stack.pop()
                lst[stack_i] = i - stack_i
            stack.append((temp, i))
        return lst
