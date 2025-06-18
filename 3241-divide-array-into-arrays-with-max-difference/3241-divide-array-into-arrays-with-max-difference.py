class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        '''
        [1,3,4,8,7,9,3,5,1], k = 2
        '''
        nums.sort()
        i = 0
        res = []

        while i < len(nums):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append([nums[i], nums[i + 1], nums[i + 2]])
            i += 3
        return res




