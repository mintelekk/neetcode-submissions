class Solution:
    def rob(self, nums: List[int]) -> int:
        one_house_ago, two_houses_ago = 0, 0
        for m in nums:
            #Recurrence Relation
            #Can include money for previous house or 
            #this current house m and two houses ago
            current = max(one_house_ago, m + two_houses_ago)
            #move to the next subproblem (next house)
            two_houses_ago = one_house_ago
            one_house_ago = current
        return one_house_ago