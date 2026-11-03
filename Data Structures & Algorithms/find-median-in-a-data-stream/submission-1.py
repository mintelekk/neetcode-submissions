import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.len1 = 0
    def addNum(self, num: int) -> None:
        
        self.len1 += 1
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) < len(self.right):
                heapq.heappush(self.left, -heapq.heappop(self.right))
            else:
                heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if self.len1 == 1:
            if len(self.left) > 0:
                return -self.left[0]
            else:
                return self.right[0]
        if self.len1 % 2 == 1:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2
        