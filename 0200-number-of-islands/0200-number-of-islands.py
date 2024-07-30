class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        
        visited = set()
        islands = 0
        
        def bfs(r,c):
            
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                
                R,C = q.popleft()
                
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                
                for dr,dc in directions:
                    row,col = R+dr,C+dc
                    
                    if (row < 0 
                        or col < 0 
                        or row >= ROWS 
                        or col >= COLS 
                        or (row,col) in visited 
                        or grid[row][col] == "0"):
                        continue
                        
                    q.append((row,col))
                    visited.add((row,col))
                    
        
        for r in range(ROWS):
            for c in range(COLS):
                
                if ( grid[r][c] == "1" and
                (r,c) not in visited):
                    bfs(r,c)
                    
                    islands+=1
                
        return islands
                    
                    
                    
                
                    
        
        
        
        