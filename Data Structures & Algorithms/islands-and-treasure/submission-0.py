from collections import deque
from typing import List
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr,nc))
                 