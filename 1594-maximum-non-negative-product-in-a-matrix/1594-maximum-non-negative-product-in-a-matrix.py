class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        modulo = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        dp_min = [[0] * n for _ in range(m)]
        dp_max = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp_min[i][j] = grid[i][j]
                    dp_max[i][j] = grid[i][j]
                else:
                    candidates = []
                    if j > 0:
                        candidates += [dp_min[i][j-1] * grid[i][j], dp_max[i][j-1] * grid[i][j]]
                    if i > 0:
                        candidates += [dp_min[i-1][j] * grid[i][j], dp_max[i-1][j] * grid[i][j]]

                    dp_min[i][j] = min(candidates)
                    dp_max[i][j] = max(candidates)

        res = dp_max[-1][-1]

        return res % modulo if res >= 0 else -1