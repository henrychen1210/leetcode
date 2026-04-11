class UF:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent, res):
        a, b = self.find(child),  self.find(parent)
        self.parents[a] = b
        return res - 1 if a != b else res

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        O(m*n)
        O(1)
        '''

        m = len(grid)
        n = len(grid[0])
        res = 0
        uf = UF(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    for dx, dy in [[1,0],[0,1]]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                            res = uf.union(i * n + j, ni * n + nj, res)
        
        return res
