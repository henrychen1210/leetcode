class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        '''
        nums = [1,1,2,3,2,1,2]

        res = min(res, x)
        i, j, k
        0, 1, 5 =  1 + 5 + 5 = 11
        '''

        res = float("inf")
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and nums[j] != nums[i]:
                j += 1
            
            k = j + 1
            while k < len(nums) and nums[k] != nums[i]:
                k += 1
            
            if j < len(nums) and k < len(nums):
                x = abs(i - j) + abs(j - k) + abs(k - i)
                res = min(res, x)
        
        return res if res != float("inf") else -1