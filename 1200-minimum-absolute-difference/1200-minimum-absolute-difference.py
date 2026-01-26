class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        min_diff = float('inf')
        arr.sort()

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                res.append([arr[i - 1], arr[i]])

        return res