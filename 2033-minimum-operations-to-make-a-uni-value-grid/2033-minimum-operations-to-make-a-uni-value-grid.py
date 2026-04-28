class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        '''
        '''

        nums = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                nums.append(grid[i][j])

        base = nums[0]
        for n in nums:
            if abs(n - base) % x != 0:
                return -1

        nums.sort()

        n = len(nums)
        median = nums[n // 2]

        ops = 0

        for n in nums:
            ops += abs(n - median) // x

        return ops 

