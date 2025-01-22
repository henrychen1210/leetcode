class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}

        for i in range(len(nums)):
            if target - nums[i] not in record:
                record[nums[i]] = i
            else:
                return [record[target - nums[i]], i]