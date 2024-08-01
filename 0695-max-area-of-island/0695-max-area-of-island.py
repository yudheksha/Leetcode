class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        maxIsland = 0
        
        def bfs(r,c):
            nonlocal maxIsland
            maxLen = 1
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                r,c = q.popleft()
                
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr,dc in directions:
                    R,C = r+dr,c+dc
                    
                    if ( R<0 or C<0 
                    or R>= ROWS or C>=COLS
                    or  grid[R][C] == 0
                    or (R,C) in visited):
                        continue
                        
                    maxLen=maxLen+1
                    q.append((R,C))
                    visited.add((R,C))
            maxIsland = max(maxIsland, maxLen)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and 
                (r,c) not in visited):
                    bfs(r,c)
        
        return maxIsland