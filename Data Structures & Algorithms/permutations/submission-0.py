class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        combination = []
        used = set()
        def dfs(i):
            if i == len(nums):
                ans.append(combination.copy())
                return

            for number in nums:
                if number in used:
                    continue
                #choose
                used.add(number)
                combination.append(number)
                dfs(i+1)
                combination.pop()
                used.remove(number)
        dfs(0)
        return ans