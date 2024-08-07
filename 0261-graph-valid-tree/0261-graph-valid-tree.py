class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        preReq = {i:[] for i in range(n)}
        
        for a,b in edges:
            preReq[a].append(b)
            preReq[b].append(a)
            
        visit = set()
        
        def dfs(i,prev):
            
            if i in visit:
                return False
            
            visit.add(i)
            
            for nei in preReq[i]:
                if nei == prev:
                    continue
                    
                if not dfs(nei,i):
                    return False
                
            return True
        
        
        return dfs(0,-1) and n == len(visit)