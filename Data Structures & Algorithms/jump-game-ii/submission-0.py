class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jump1 = nums[0]
        ans = 0
        end = len(nums)-1
        while i < end:
            #+1 jump required
            ans += 1
            #If can reach end end
            if jump1 + i >= end:
                return ans
            #Find max jump power
            maxJump = jump1
            maxJumpStatic = jump1
            i_0 = i
            while jump1 > 0:
                jump1 -= 1
                maxJump -= 1
                i += 1
                if nums[i] > maxJump:
                    i_0 = i
                    maxJump = nums[i]
                    maxJumpStatic = maxJump
            #New jump power and new location
            jump1 = maxJumpStatic
            i = i_0
            print(i, jump1)
        return ans