class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if i != i2 and n + n2 == target:
                    return [i, i2]