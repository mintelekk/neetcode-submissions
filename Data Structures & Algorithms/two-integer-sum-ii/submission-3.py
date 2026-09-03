class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = set()
        for n in numbers:
            hashset.add(n)
        for i, n in enumerate(numbers):
            if target - n in hashset:
                if target - n == n:
                    return [i+1,i+2]
                return [i+1, numbers.index(target-n) + 1]