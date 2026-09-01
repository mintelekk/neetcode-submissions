class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sortedNums = sorted(nums)
        ans = 1
        consec = 1
        for i in range(len(nums) -1):
            if sortedNums[i]== sortedNums[i+1]-1:
                consec += 1
                if consec > ans:
                    ans = consec
            elif sortedNums[i] == sortedNums[i+1]:
                #Skip
                pass
            else:
                consec = 1
        return ans