class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = max(heights)
        l, r = 0, len(heights) -1
        maxArea = 0
        while l < r:
            currentWaterH = min(heights[l], heights[r])
            currentArea = currentWaterH * (r-l)
            if currentArea > maxArea:
                maxArea = currentArea
            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                l+=1
                r-=1
        return maxArea