class Solution:
    def numIslands(self, grid1: List[List[str]]) -> int:
        def dfs(r, c):
            grid1[r][c] = "0"
            if r > 0 and grid1[r-1][c] == "1":
                dfs(r-1, c)
            if r < len(grid1)-1 and grid1[r+1][c] == "1":
                dfs(r+1,c)
            if c > 0 and grid1[r][c-1] == "1":
                dfs(r, c-1)
            if c < len(grid1[0])-1 and grid1[r][c+1] == "1":
                dfs(r,c+1)
        ans = 0
        for r, rl in enumerate(grid1):
            for c, cs in enumerate(grid1[0]):
                if grid1[r][c] == "1":
                    dfs(r,c)
                    ans += 1
        return ans