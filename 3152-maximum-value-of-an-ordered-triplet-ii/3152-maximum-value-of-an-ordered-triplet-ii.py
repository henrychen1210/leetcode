class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        '''
        [12,6,1,2,7]
        (12 - 1) * 7 = 
        nums[j] min
        nums[i], nums[k] max
        '''
        N = len(nums)
        prefix_max = [0] * N
        suffix_max = [0] * N
        for i in range(1, N):
            prefix_max[i] = max(nums[i - 1], prefix_max[i - 1])
        
        for j in range(N - 2, -1, -1):
            suffix_max[j] = max(nums[j + 1], suffix_max[j + 1])
        
        result = 0
        for i in range(1, N - 1):
            result = max((prefix_max[i] - nums[i]) * suffix_max[i], result)
        
        return result
