class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = 0
        col = 0
        rowHashmap = dict()
        colHashmap = dict()
        gridHashmap = dict()
        for i in range(9):
            rowHashmap[i] = set()
            colHashmap[i] = set()
            gridHashmap[i] = set()
        priorityQueue = []
        for i, r in enumerate(board):
            for i2, c in enumerate(r):
                if c == ".":
                    priorityQueue.append((i,i2))
                else:
                    n = int(c)
                    if n in rowHashmap[i]:
                        return False
                    rowHashmap[i].add(n)
                    if n in colHashmap[i2]:
                        return False
                    colHashmap[i2].add(n)
                    if n in gridHashmap[(i//3) * 3 + (i2//3)]:
                        return False
                    gridHashmap[(i//3) * 3 + (i2//3)].add(int(c))
        return True
        #End of solution
        #Extra effort: Check if suduko board is solvable
        currentIterations = 0
        while priorityQueue and currentIterations < 81:
            #Check next empty node for answer.
            r,c = priorityQueue.pop(0)
            #Check row, col, and grid set
            possibleRow = set(range(1,10)) - rowHashmap[r]
            possibleCol =  set(range(1,10)) - colHashmap[c]
            possibleGrid = set(range(1,10)) - gridHashmap[(r//3)*3 + (c//3)]
            #Intersection of three possible sets is answers to this node
            possibleAns = possibleRow & possibleCol & possibleGrid
            if len(possibleAns) == 1:
                #Solution for current empty node found.
                certainAns = possibleAns.pop()
                #Add to sets new non empty node.
                rowHashmap[r].add(certainAns)
                colHashmap[c].add(certainAns)
                gridHashmap[(i//3) * 3 + (i2//3)].add(certainAns)
                currentIterations = 0
            else:
                priorityQueue.append((r,c))
                currentIterations += 1
        if not priorityQueue:
            return True
        return False
