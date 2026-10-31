import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = None
            if len(max_heap) > 0:
                stone2 = -heapq.heappop(max_heap)
                if stone1 == stone2:
                    #Both destroyed
                    pass
                elif stone1 < stone2:
                    stone2= stone2-stone1
                    heapq.heappush(max_heap, -stone2)
                else:
                    stone1= stone1-stone2
                    heapq.heappush(max_heap, -stone1)
        if len(max_heap) == 1:
            return -heapq.heappop(max_heap)
        else:
            return 0