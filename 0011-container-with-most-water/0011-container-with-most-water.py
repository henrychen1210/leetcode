class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        height = [1,8,6,2,5,4,8,3,7]

        left, right = 0, len(height) - 1
        res 

        min(height[left], higtht[right]) * right - left + 1

        '''


        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            res = max(res, curr)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return res

