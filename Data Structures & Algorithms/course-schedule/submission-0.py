class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        def dfs(adj, u, visited, recStack):
            #Node is already in the current DFS path
            if recStack[u]:
                return True
            
            #Node is already visited
            if visited[u]:
                return False
            visited[u] = True
            recStack[u] = True

            #visit all adjacent nodes
            for v in adj[u]:
                if dfs(adj, v, visited, recStack):
                    return True

            #Remove node from current DFS path
            recStack[u] = False
        
            return False
        visited = [False] * numCourses
        recStack = [False] * numCourses

        #Check all components
        for i in range(numCourses):
            if not visited[i] and dfs(adj, i, visited, recStack):
                return False
        return True