class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        '''
        [3, 7] 
        prefix [0, 3, 10]
        sufix [19, 7, 0]
        [5, 5]
        pre [0, 5, 10], su [10, 5, 0]
        '''
        m = len(grid)
        n = len(grid[0])

        vertical = [0] * n
        horizontal = [0] * m

        for i in range(m):
            for j in range(n):
                horizontal[i] += grid[i][j]
        
        for j in range(n):
            for i in range(m):
                vertical[j] += grid[i][j]
        
        v_prefix = [0] * n
        for i in range(1, n):
            v_prefix[i] = vertical[i - 1] + v_prefix[i - 1]
        
        v_sufix = vertical[n - 1]
        for i in range(n - 1, 0, -1):
            if v_sufix == v_prefix[i]:
                return True
            v_sufix += vertical[i - 1]
            
        h_prefix = [0] * m
        for i in range(1, m):
            h_prefix[i] = horizontal[i - 1] + h_prefix[i - 1]
        
        h_sufix = horizontal[m - 1]
        for i in range(m - 1, 0, -1):
            if h_sufix == h_prefix[i]:
                return True
            h_sufix += horizontal[i - 1]
        
        return False

        






