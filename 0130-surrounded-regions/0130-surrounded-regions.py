class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS = len(board)
        COLS = len(board[0])
        
        visited = set()
        
        def dfs(r,c):
            if (r<0 
               or r == ROWS
               or c<0
               or c == COLS
               or (r,c) in visited
               or board[r][c] == "X"):
                return
            
            board[r][c] = "T"
            visited.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            
        for c in range(COLS):
            dfs(0,c)
            
        for c in range(COLS):
            dfs(ROWS-1,c)
            
        for r in range(ROWS):
            dfs(r,0)
            
        for r in range(ROWS):
            dfs(r,COLS-1)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
                else:
                    board[r][c] = "X"
            
            
        