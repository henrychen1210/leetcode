class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        '''
        nums = [1,2,1,1,3]
        map = {1: [0]}


        i, map, res
        0, {1: [0]} x
        1, {1:[0], 2:[1]} X
        2, {1:[0, 2], 2:[1]} X
        3, {1:[0, 2, 3] 2: [1]}, 6

        i, j, k
        '''

        memo = {}
        res = float('inf')

        for k in range(len(nums)):
            if nums[k] not in memo:
                memo[nums[k]] = []
            memo[nums[k]].append(k)

            if len(memo[nums[k]]) >= 3:
                j, i = memo[nums[k]][-2], memo[nums[k]][-3]
                x = abs(i - j) + abs(j - k) + abs(k - i)
                res = min(res, x)
        
        return res if res != float('inf') else -1