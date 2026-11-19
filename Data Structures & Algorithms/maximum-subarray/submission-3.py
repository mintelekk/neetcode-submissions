class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        sum1 = 0
        for i, n in enumerate(nums):
            sum1 += nums[i]
            if sum1 > maxSum:
                maxSum = sum1
            if sum1 <= 0:
                sum1 = 0
        return maxSum       

