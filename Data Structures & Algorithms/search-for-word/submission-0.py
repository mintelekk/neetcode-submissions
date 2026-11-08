class Solution:
    def startSpot(self, c, board):
        coords = []
        for r in range(len(board)):
            for c2 in range(len(board[0])):
                if board[r][c2] == c:
                    coords.append((r,c2))
        return coords
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        combinations = []
        coords = self.startSpot(word[0], board)
        visited = set()
        def dfs(r, c, index):
            if r >= len(board) or r < 0 or c < 0 or c >= len(board[0]):
                return False
            if (r,c) in visited:
                return False
            if board[r][c] != word[index]:
                return False
            if index == len(word)-1:
                return True
            visited.add((r,c))
            #Explore 4 neighbors
            for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                if dfs(r+dr,c+dc,index+1):
                    visited.remove((r,c))
                    return True
            #Back Track
            visited.remove((r,c))
            return False
        ans = False
        print(coords)
        for r,c in coords:
            ans = ans or dfs(r,c,0)
        return ans