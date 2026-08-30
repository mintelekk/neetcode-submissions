class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix= [1 for x in nums]
        suffix = [1 for x in nums]
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        ans = []
        for p, s in zip(prefix, suffix):
            ans.append(p*s)
        return ans