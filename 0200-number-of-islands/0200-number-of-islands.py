
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        O(m*n)
        O(1)
        '''

        res = 0
        m = len(grid)
        n = len(grid[0])

        dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def helper(x, y): 
            queue = collections.deque()
            grid[x][y] = "0"
            queue.append([x, y])

            while queue:
                i, j = queue.popleft()
                
                for di, dj in dirs:
                    if 0 <= i + di < m and 0 <= j + dj < n:
                        if grid[i + di][j + dj] == "1":
                            grid[i + di][j + dj] = "0"
                            queue.append([i + di, j + dj])
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    helper(i, j)
                    res += 1
        
        return res
