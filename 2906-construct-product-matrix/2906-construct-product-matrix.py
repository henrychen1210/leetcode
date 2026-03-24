class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m = len(grid)
        n = len(grid[0])
        prefix = [[0] * n for _ in range(m)]
        sufix = [[0] * n for _ in range(m)]
        p = [[0] * n for _ in range(m)]

        # Build prefix (product of all elements before [i][j] in row-major order)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix[i][j] = 1
                elif j == 0:
                    prefix[i][j] = prefix[i-1][n-1] * grid[i-1][n-1] % mod
                else:
                    prefix[i][j] = prefix[i][j-1] * grid[i][j-1] % mod

        # Build suffix (product of all elements after [i][j] in row-major order)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    sufix[i][j] = 1
                elif j == n-1:
                    sufix[i][j] = sufix[i+1][0] * grid[i+1][0] % mod
                else:
                    sufix[i][j] = sufix[i][j+1] * grid[i][j+1] % mod

        # Combine
        for i in range(m):
            for j in range(n):
                p[i][j] = prefix[i][j] * sufix[i][j] % mod

        return p