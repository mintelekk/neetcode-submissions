from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        if len(edges) == 0:
            return True
        adj = {c:[] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        #Breadth First Search Solution
        queue = deque()
        queue.append(edges[0][0])
        visited = set()
        while queue:
            u = queue.popleft()
            if u in visited:
                return False
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    queue.append(v)
        for i in range(n):
            if i not in visited:
                return False
        return True