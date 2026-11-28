class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for m in nums:
            current = max(rob2, m + rob1)
            rob1 = rob2
            rob2 = current
        return rob2