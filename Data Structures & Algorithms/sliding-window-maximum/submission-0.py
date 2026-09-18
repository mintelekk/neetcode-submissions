class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElem = max(nums[0:k])
        ans = [10001]*(len(nums)-k+1)
        l, r = 0, k-1
        while r < len(nums):
            if l > 0 and nums[l-1] == maxElem:
                maxElem = max(nums[l:r+1])
            else:
                maxElem = max(maxElem, nums[r])
            ans[l] = maxElem
            l += 1
            r += 1

        return ans