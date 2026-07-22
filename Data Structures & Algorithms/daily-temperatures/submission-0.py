class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_i, stack_temp = stack.pop()
                ans[stack_i] = i - stack_i
            stack.append((i, temp))
        return ans