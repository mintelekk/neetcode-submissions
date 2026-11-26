import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res, i = {}, 0
        #Iterate over querie points
        for q in sorted(queries):
        #Find each interval where start is less than equal to q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                #Use min heap to store size of intervals
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            #Trim min heap from previously ended intervals
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            #Add to hashmap answer for current query
            res[q] = minHeap[0][0] if minHeap else -1
        #Convert hashmap answer to list answer
        return [res[q] for q in queries]