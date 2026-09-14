class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []   # indices, temperatures decreasing

        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                j = stack.pop()
                out[j] = i - j
            stack.append(i)

        return out