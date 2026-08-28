class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set1= set()
        for n in nums:
            set1.add(n)
        for i, n in enumerate(nums):
            n2 = target-n
            if n2 in set1:
                if n2 == n:
                    if nums[i+1:].count(n2) > 0:
                        return [i, nums[i+1:].index(n2)+i+1]
                else:
                    return sorted([i, nums.index(n2)])