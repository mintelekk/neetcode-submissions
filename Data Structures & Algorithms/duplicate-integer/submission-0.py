class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for n in nums:
            if n in dict1.keys():
                dict1[n] = dict1[n] + 1
            else:
                dict1[n] = 1
        for n in dict1.values():
            if n > 1:
                return True
        return False