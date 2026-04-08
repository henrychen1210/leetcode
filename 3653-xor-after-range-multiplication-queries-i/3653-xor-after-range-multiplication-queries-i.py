class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        '''
        [1,1,1], queries = [[0,2,1,4]]

        idx = 0
        idx = 2

        nums[idx] = (nums[idx] * 4) % (10**9 + 7)

        idk + 1
        '''



        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k

        res = 0
        for x in nums:
            res ^= x
            
        return res