class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                #bfs the islands, increase the counter and remove the already counted islands
                if grid[r][c] == "1":
                    res += 1
                    queue = deque()
                    queue.append((r,c))
                    while queue:
                        #get next co-ord from queue
                        ro,co = queue.popleft()
                        #change to a 0
                        grid[ro][co] = "0"
                        #check all surrounding squares and add "1"s to queue 
                        if ro+1 < ROWS and grid[ro+1][co] == "1":
                            grid[ro+1][co] = "0"
                            queue.append((ro+1,co))
                        if ro-1 >= 0 and grid[ro-1][co] == "1":
                            grid[ro-1][co] = "0"                            
                            queue.append((ro-1,co))
                        if co+1 < COLS and grid[ro][co+1] == "1":
                            grid[ro][co+1] = "0" 
                            queue.append((ro,co+1))
                        if co-1 >= 0 and grid[ro][co-1] == "1":
                            grid[ro][co-1] = "0" 
                            queue.append((ro,co-1))
        
        return res
                                  