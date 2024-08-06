class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preReq = {i:[] for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            preReq[crs].append(prereq)
            
        
        visit = [0]*numCourses
        result =[]
        
        def dfs(crs):
            
            if visit[crs]==-1:
                return True
            
            if visit[crs]==1:
                return False
            
            visit[crs]=1
            
            for nei in preReq[crs]:
                if not dfs(nei):
                    return False
                
            visit[crs]=-1
            result.append(crs)
            return True
        
        
        
        for crs in range(numCourses):
            if visit[crs]==0:
                if not dfs(crs):
                    return []
            
        return result