class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        left, right = 0, 0
        zero = 0
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        
        res = max(res, right - left = 1)

        left, rihgt, zero
        0, 0, 0 [1]
        0, 1, 0 [1, 1]
        ;
        ;
        0, 3, 1 [1,1,1,0]
        0, 4, 2 [1,1,1,0,0]
        0, 5, 3 [1,1,1,0,0,0] X -> 1, 5, 3 [1,1,0,0,0] -> 4, 5, 2, [0,0] 
        '''

        left = 0
        zero = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            
            while zero > k and left <= right:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            if zero <= k:
                res = max(res, right - left + 1)
        
        return res