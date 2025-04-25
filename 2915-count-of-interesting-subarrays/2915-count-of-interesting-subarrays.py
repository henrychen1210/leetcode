class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        '''

        '''
        n = len(nums)
        prefix = 0
        res = 0
        count = {0: 1}

        for i in range(n):
            if nums[i] % modulo == k:
                prefix += 1

            res += count.get((prefix - k + modulo) % modulo, 0)

            count[prefix % modulo] = count.get(prefix % modulo, 0) + 1

        return res 
        

        