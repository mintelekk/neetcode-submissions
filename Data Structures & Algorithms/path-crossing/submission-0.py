class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        x, y = 0,0
        s.add((x,y))
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x -= 1
            else:
                x += 1
            if (x,y) in s:
                return True
            s.add((x,y))
        return False