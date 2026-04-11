class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        '''

        res = 0
        m = len(grid)
        n = len(grid[0])

        dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def helper(x, y): 
            if grid[x][y] == "0": return

            for dx, dy in dirs:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    helper(x + dx, y + dy)
                grid[x][y] ="0"
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    helper(i, j)
                    res += 1
        
        return res
            
