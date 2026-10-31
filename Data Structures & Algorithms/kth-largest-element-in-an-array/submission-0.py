import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap1 = [-n for n in nums]
        heapq.heapify(heap1)

        for i in range(k-1):
            heapq.heappop(heap1)

        return -heapq.heappop(heap1)