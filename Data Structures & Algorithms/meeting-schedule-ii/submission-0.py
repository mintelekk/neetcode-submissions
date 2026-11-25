import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key= lambda x: x.start)
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, intervals[0].end)
        for i in intervals[1:]:
            #Min heap earliest available room
            if i.start >= heap[0]:
                heapq.heappop(heap)
            #Assign a room to the meeting
            heapq.heappush(heap, i.end)
        return len(heap)