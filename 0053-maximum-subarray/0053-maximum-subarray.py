class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        '''

        currSum = 0
        res = float('-inf')

        for n in nums:
            currSum += n
            res = max(res, currSum)

            if currSum < 0:
                currSum = 0
            
        return res