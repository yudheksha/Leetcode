class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        ROWS = len(rooms)
        COLS = len(rooms[0])
        
        q = deque()
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
                    
                    
                    
        dist = 0
        while q:
            for i in range(len(q)):
                
                R,C = q.popleft()
                rooms[R][C] = dist
                
                distances = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr,dc in distances:
                    newRow, newCol = R+dr, C+dc
                    
                    if (newRow < 0 or newRow == ROWS 
                        or newCol <0 or newCol == COLS
                        or (newRow,newCol) in visited
                        or rooms[newRow][newCol] == -1):
                        continue
                        
                    q.append([newRow,newCol])
                    visited.add((newRow,newCol))
                
                             
                             
            dist+=1
                
                             
                        
                    
                
            
            
        