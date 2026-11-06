class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates_sorted = sorted(candidates)
        combination = []

        def dfs(i, remaining):
            if remaining == 0:
                ans.append(combination.copy())
                return
            if i >= len(candidates) or remaining < 0:
                return

            combination.append(candidates_sorted[i])
            dfs(i+1, remaining-candidates_sorted[i])
            combination.pop()


            while i + 1 < len(candidates_sorted) and candidates_sorted[i] == candidates_sorted[i+1]:
                i += 1
            dfs(i+1, remaining)

            return
        dfs(0, target)

        return ans