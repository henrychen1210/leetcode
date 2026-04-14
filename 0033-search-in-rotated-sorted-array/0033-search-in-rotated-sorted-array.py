class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        nums = [4,5,6,7,0,1,2], target = 0

        left, mid, right
        4, 7, 2

        '''


        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return mid

            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:   
                    left = mid + 1
            
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        
        return -1