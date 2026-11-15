class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()
        #DFS detect cycle
        def dfs(crs):
            #Visited means cycle
            if crs in visited:
                return True
            #end of graph means no cycle
            if preMap[crs] == []:
                return False
            #Recursive DFS
            visited.add(crs)
            for crs2 in preMap[crs]:
                if dfs(crs2):
                    return True
            visited.remove(crs)
            #Memoize the path after checking each path in for loop
            #Do not need to check path again. We know it has no cycle.
            #(Return false)
            preMap[crs] = []
            return False

        for c in range(numCourses):
            #if cycle then return False cannot finish all courses
            if dfs(c):
                return False
        #if no cycle return true can finish all courses.
        return True