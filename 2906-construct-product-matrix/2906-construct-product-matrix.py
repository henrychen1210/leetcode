class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m = len(grid)
        n = len(grid[0])
        p = [[0] * n for _ in range(m)]

        prefix = 1
        for i in range(m):
            for j in range(n):
                p[i][j] = prefix
                prefix = prefix * grid[i][j] % mod

        sufix = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                p[i][j] = (p[i][j] * sufix) % mod
                sufix = sufix * grid[i][j] % mod

        return p