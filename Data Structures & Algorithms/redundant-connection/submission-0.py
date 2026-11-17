class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n+1)]
        answer = []

        def has_path(start, target):
            visited = set()
            stack = [start]

            while stack:
                node = stack.pop()

                if node == target:
                    return True
                
                if node in visited:
                    continue

                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            return False

        for u,v in edges:
            if has_path(u, v):
                answer = [u, v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return answer