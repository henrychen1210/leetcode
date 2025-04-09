class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        '''
        nums = [5,2,5,4,5], k = 2
        [3, 0, 3, 2, 3]
        h = 4, [4, 2, 4, 4, 4]
        h = 2, [2, 2, 2, 2, 2]

        nums = [2,1,2], k = 2
        [0, -1, 0]
        nums = [9,7,5,3], k = 1
        [8, 6, 4, 2]
        '''

        record = set()
        n = len(nums)
        for i in range(n):
            if nums[i] - k > 0:
                record.add(nums[i] - k)
            elif nums[i] - k < 0:
                return -1
        
        return len(record)





