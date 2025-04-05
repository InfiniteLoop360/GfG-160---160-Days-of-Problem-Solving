class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        # Directions: 8 directions (including diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def dfs(i, j):
            visited[i][j] = True
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if not visited[ni][nj] and grid[ni][nj] == 'L':
                        dfs(ni, nj)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
                    
        return count
