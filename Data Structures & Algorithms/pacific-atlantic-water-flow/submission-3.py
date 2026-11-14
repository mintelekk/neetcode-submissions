class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        pacificStartingCells= []
        atlanticStartingCells = []
        rows = len(heights)
        cols = len(heights[0])
        for i in range(rows):
            pacificStartingCells.append((i,0))
            atlanticStartingCells.append((i,cols-1))
        for i in range(cols):
            pacificStartingCells.append((0,i))
            atlanticStartingCells.append((rows-1,i))
        def dfs(r,c, s):
            s.add((r,c))
            if r > 0 and (r-1, c) not in s and heights[r-1][c] >= heights[r][c]:
                dfs(r-1,c,s)
            if r < rows -1 and (r+1, c) not in s and heights[r+1][c] >= heights[r][c]:
                dfs(r+1,c,s)
            if c > 0 and (r, c-1) not in s and heights[r][c-1] >= heights[r][c]:
                dfs(r,c-1,s)
            if c < cols-1 and (r, c+1) not in s and heights[r][c+1] >= heights[r][c]:
                dfs(r,c+1,s)
        for r,c in pacificStartingCells:
            if (r,c) not in pacific:
                dfs(r,c,pacific)
        for r,c in atlanticStartingCells:
            if (r,c) not in atlantic:
                dfs(r,c,atlantic)

        return [list(cell) for cell in (pacific & atlantic)]