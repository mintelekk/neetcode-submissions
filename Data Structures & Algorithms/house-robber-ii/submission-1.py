class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            one_house_ago, two_houses_ago = 0, 0
            for m in houses:
                current = max(one_house_ago, m + two_houses_ago)
                two_houses_ago = one_house_ago
                one_house_ago = current
            return one_house_ago
        #Exclude the last house and exclude the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))