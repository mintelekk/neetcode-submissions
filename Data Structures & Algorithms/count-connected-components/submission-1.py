class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {c:[] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        ans = 0
        def dfs(u):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)
        size = 0
        for i in range(n):
            dfs(i)
            if len(visited) > size:
                size = len(visited)
                ans += 1
        return ans