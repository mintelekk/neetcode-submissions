class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        prevEnd = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < prevEnd:
                #If overlap greedily remove the interval that ends last
                prevEnd = min(prevEnd, i[1])
                ans += 1
            else:
                #If no overlap update previous end
                prevEnd = i[1]
        return ans