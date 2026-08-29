class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for n in nums:
            if n in dict1:
                dict1[n] = dict1[n] + 1    
            else:
                dict1[n] = 1
        mostFrequent = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in mostFrequent[:k]]