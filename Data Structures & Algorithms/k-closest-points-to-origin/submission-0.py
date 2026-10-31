import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclideanDist = []
        heapq.heapify(euclideanDist)
        for p in points:
            heapq.heappush(euclideanDist, ((math.sqrt((p[0]-0)**2+(p[1]-0)**2)), p[0], p[1]))
        return [[p[1], p[2]] for p in (heapq.heappop(euclideanDist) for _ in range(k))]