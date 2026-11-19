class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i = 0
        jump = nums[0]
        while i < len(nums)-1:
            if jump > 0:
                jump -= 1
                i+=1
            else:
                return False
            if nums[i] > jump:
                jump = nums[i]
            print(i, jump)

        return True