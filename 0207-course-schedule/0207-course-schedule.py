class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
            
        
        visit = [0]*numCourses
        
        def dfs(crs):
            
            if visit[crs] == 1:
                return False
            
            if preMap[crs] == []:
                return True
            
            visit[crs]=1
            
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
                
            visit[crs]=0
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        
        return True
        
        