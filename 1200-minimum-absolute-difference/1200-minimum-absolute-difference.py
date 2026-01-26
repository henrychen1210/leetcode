class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        min_abs = float('inf')
        arr.sort()

        for i in range(1, len(arr)):
            min_abs = min(min_abs, arr[i] - arr[i - 1])
        for i in range(1, len(arr)):
            print(arr[i], arr[i - 1])
            if arr[i] - arr[i - 1] == min_abs:
                res.append([arr[i - 1], arr[i]])
        
        return res