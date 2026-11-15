class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in visited:
                    edge = False
                    current = []
                    stack = [(r, c)]
                    visited.add((r, c))
                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        current.append((curr_r, curr_c))
                        if curr_r == 0 or curr_r == rows - 1 or curr_c == 0 or curr_c == cols - 1:
                            edge = True
                        for dr, dc in directions:
                            r2, c2 = curr_r + dr, curr_c + dc
                            if 0 <= r2 < rows and 0 <= c2 < cols and board[r2][c2] == 'O' and (r2, c2) not in visited:
                                visited.add((r2, c2))
                                stack.append((r2, c2))
                    
                    if not edge:
                        for r2, c2 in current:
                            board[r2][c2] = 'X'