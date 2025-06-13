class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        '''
        [1,2,2,4]
        '''
        nums.sort()
        n = len(nums)
        
        def can_form_pairs(max_diff):
            index, count = 0, 0
            while index < n - 1:
                if nums[index + 1] - nums[index] <= max_diff:
                    count += 1
                    index += 1
                index += 1
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if can_form_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left

