class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        merged = None
        i = 0
        while i < len(intervals):
            if i < len(intervals) - 1 and sorted_intervals[i][1] >= sorted_intervals[i+1][0]:
                merged = [sorted_intervals[i][0], max(sorted_intervals[i+1][1], sorted_intervals[i][1])]
                i2 = i + 1
                while i2 < len(intervals) - 1 and merged[1] >= sorted_intervals[i2+1][0]:
                    merged[1] = max(merged[1], sorted_intervals[i2+1][1])
                    i2 += 1
                i = i2
                res.append(merged)
            else:
                res.append(sorted_intervals[i])
            i+=1
        return res
