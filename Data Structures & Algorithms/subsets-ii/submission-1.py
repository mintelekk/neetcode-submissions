class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        combination = []
        included = set()

        def dfs(i):
            #Recursive base case 
            if i == len(nums):
                ans.append(combination.copy())
                return

            #Build combination
            included.add(nums[i])
            combination.append(nums[i])
            dfs(i+1)

            included.discard(nums[i])
            #Skip extra backtracking for duplicate answers when same num
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            combination.pop()
            dfs(i+1)

        dfs(0)
        return ans