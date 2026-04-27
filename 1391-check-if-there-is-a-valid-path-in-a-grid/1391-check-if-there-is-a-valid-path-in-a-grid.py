class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        '''
        set()


        '''

        streets = {
            1: [2, 4],
            2: [1, 3],
            3: [3, 4],
            4: [2, 3],
            5: [1, 4],
            6: [1, 2]
        }

        n = len(grid)
        m = len(grid[0])

        q = collections.deque()
        q.append([0, 0])
        visited = set()

        while q:
            x, y = q.popleft()
            idx = grid[x][y]

            if x == n - 1 and y == m - 1:
                return True

            if (x, y) in visited:
                continue
            
            visited.add((x, y))

            if (x + 1 < n and 
                3 in streets[idx] and 
                1 in streets[grid[x + 1][y]]
            ):
                q.append([x + 1, y])
            

            if (y + 1 < m and 
                2 in streets[idx] and 
                4 in streets[grid[x][y + 1]]
            ):
                q.append([x, y + 1])

            if (x - 1 >= 0 and 
                1 in streets[idx] and 
                3 in streets[grid[x - 1][y]]
            ):
                q.append([x - 1, y])
            

            if (y - 1 >= 0 and 
                4 in streets[idx] and 
                2 in streets[grid[x][y - 1]]
            ):
                q.append([x, y - 1])
            
        return False


