class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        preReq = {i:[] for i in range(n)}
        
        for a,b in edges:
            preReq[a].append(b)
            preReq[b].append(a)
            
            
        visit = set()
        connComp = 0
        
        def dfs(i, prev):
            visit.add(i)
            
            for nei in preReq[i]:
                if nei!=prev and nei not in visit:
                    dfs(nei,i)
            return 
        
        
        for i in range(n):
            if i not in visit:
                connComp+=1
                dfs(i,-1)
                
        return connComp