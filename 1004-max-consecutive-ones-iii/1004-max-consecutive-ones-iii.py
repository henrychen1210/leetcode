class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        res = max(res, len(wondow)) 

            zero
        [1] 0
        [1,1] 0
        [1,1,1] 0
        [1,1,1,0] 1
        [1,1,1,0,0] 2
        [1,1,1,0,0,0] 3 X -> [1,1,0,0,0] 3 x -> ... -> [0,0] 2
        [0,0,1] 2
        []  

        Time O(n)
        Space O(1)

        '''

        left = 0
        zero = 0
        res = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zero += 1

            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
