class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Build adjacency matrix
        adj = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            #Cycle detected -> False
            if crs in cycle:
                return False
            #Pass on true
            if crs in visit:
                return True
            cycle.add(crs)
            #Recurse on neighbors
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            #remove from cycle for next dfs
            cycle.remove(crs)
            #visited
            visit.add(crs)
            #Building Topological sorted order
            output.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output 