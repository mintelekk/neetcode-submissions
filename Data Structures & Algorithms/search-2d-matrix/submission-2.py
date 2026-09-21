class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLength = len(matrix[0])
        l,r = 0, (len(matrix)*rowLength)-1
        print(matrix)
        while l <= r:
            io = (l+r) // 2
            i = io % rowLength
            row = io // rowLength
            print(io, matrix[row][i])
            if matrix[row][i] == target:
                return True
            elif matrix[row][i] < target:
                l = io+1
            else:
                r = io-1
        return False