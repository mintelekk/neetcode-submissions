class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [0]
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                prev_idx = s.pop()
                ans[prev_idx] = i - prev_idx
            s.append(i)
        return ans