class PrefixTree:

    def __init__(self):
        self.map1 = {}
        self.isEnd = False
        self.word = None
    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.map1:
                curr.map1[ch] = PrefixTree()
            curr = curr.map1[ch]
        curr.isEnd = True
        curr.word = word

    

def searchBoard(board, char):
    ans = []
    for i, l in enumerate(board):
        for i2, c in enumerate(l):
            if c == char:
                ans.append((i,i2))
    return ans

def searchSpot(board, char, coordinate):
    ans = []
    i,i2 = coordinate
    if i-1 >= 0 and board[i-1][i2] == char:
        ans.append((i-1,i2))
    if i+1 < len(board) and board[i+1][i2] == char:
        ans.append((i+1,i2))
    if i2-1 >= 0 and board[i][i2-1] == char:
        ans.append((i,i2-1))
    if i2+1 < len(board[0]) and board[i][i2+1] == char:
        ans.append((i,i2+1))
    return ans
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for w in words:
            trie.insert(w)

        rows, cols = len(board), len(board[0])
        ans = []
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.map1:
                return
            curr_node = node.map1[char]
            if curr_node.word:
                ans.append(curr_node.word)
                curr_node.word = None  # Prevent duplicates
            board[r][c] = '#'
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
            board[r][c] = char


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return ans