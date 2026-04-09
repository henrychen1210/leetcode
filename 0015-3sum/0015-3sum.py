class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        nums = [-1,0,1,2,-1,-4]
        nums = [-4, -1, -1, 0, 1, 2]

        idx = 0 , -4 find 0 - (- 4) = 4

        left, right
        1, 5, 1 < 4
        3, 5, 2 < 4
        4, 5, 3 < 4

        [-4, -1, -1, 0, | 1, 2]
        i = 0
        left, right, x
        1, 5, 4, s = 1
        3, 5, 4, s = 2
        4, 5, 4, s = 3

        i = 1
        left, right, x
        '''

        nums.sort()
        res = []

        for i, n in enumerate(nums): # [-4, -1, -1, 0, 1, 2], [[-4, -1, -1, 0]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1 

            while left < right: 
                s = nums[left] + nums[right]
                x = - n

                if s == x:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < x:
                    left += 1
                else:
                    right -= 1
            
        return res
