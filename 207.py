class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)} # 1.initialize dict
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            pres = preMap[crs]
            visit.add(crs)
            for pre in pres: 
                if not dfs(pre): #2.return backtracking return value is important
                    return False
            preMap[crs] = []
            visit.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
