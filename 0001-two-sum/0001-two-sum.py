class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [2,7,11,15], target = 9
        {
            2: 0, 7: 1, 11: 2, 15: 3 
        }

        9 - 2 = 7
        '''
        index_map = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in index_map:
                return [index_map[x], i]
            
            index_map[nums[i]] = i
        
        return None