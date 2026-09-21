class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLength = len(matrix[0])
        l,r = 0, (len(matrix)*rowLength)-1
        print(matrix)
        while l <= r:
            #Binary search on consequetive lists in matrix 2d
            io = (l+r) // 2
            i = io % rowLength
            row = io // rowLength
            print(io, matrix[row][i])
            if matrix[row][i] == target:
                return True
            elif matrix[row][i] < target:
                #io is full index
                #row and i are 2d matrix index
                l = io+1
            else:
                r = io-1
        return False