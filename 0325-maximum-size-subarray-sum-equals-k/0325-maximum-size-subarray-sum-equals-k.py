class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        psum = res = 0
        indices = {}

        for i, num in enumerate(nums):
            psum += num

            if psum == k:
                res = i + 1
            
            if psum - k in indices:
                res = max(res, i - indices[psum - k])
            
            if psum not in indices:
                indices[psum] = i
        
        return res