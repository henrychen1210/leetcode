class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        '''
        [12,21,45,33,54]
        
        i, memo, res
        0, { "21": 0 }, inf
        1, { "21": 0, 12": 1 }, 1
        '''
            
        memo = {}
        res = float('inf')


        for i, n in enumerate(nums):
            strN = str(n)
            if strN in memo:
                res = min(res, i - memo[strN])

            strN = strN[::-1]

            while strN[0] == "0":
                strN = strN[1:]
            memo[strN] = i
            

        return res if res != float('inf') else -1