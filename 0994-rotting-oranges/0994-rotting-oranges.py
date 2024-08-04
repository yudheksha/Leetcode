class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        q = deque()
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    
                    
        time = 0
        while q:
            for i in range(len(q)):
                
                R,C = q.popleft()
                
                grid[R][C] = 2
                
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                
                for dr,dc in directions:
                    newRow, newCol = R+dr, C+dc
                    
                    if (newRow < 0
                        
                       or newCol <0
                       or newRow == ROWS 
                       or newCol == COLS
                       or (newRow, newCol) in visited 
                        or grid[newRow][newCol] == 0):
                        continue
                        
                    q.append((newRow,newCol))
                    visited.add((newRow,newCol))
                    
            if q:
                time+=1
                
        for row in grid:
            if 1 in row:
                return -1
        
        return time
                    
                    
    
        