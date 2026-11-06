class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        combination = []
        sum = 0
        def dfs(i, remaining):
            if remaining == 0:
                ans.append(combination.copy())
                return
            if i == len(nums) or remaining < 0:
                return
            
            combination.append(nums[i])
            dfs(i, remaining - nums[i])

            combination.pop()
            dfs(i+1, remaining)
        dfs(0, target)
        return ans