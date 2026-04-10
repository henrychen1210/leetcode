class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        last = {}  # val -> [prev_index, last_index]
        res = float("inf")

        for k, c in enumerate(nums):
            if c in last:
                j = last[c][-1]
                if len(last[c]) > 1:
                    i = last[c][-2]
                    x = abs(i - j) + abs(j - k) + abs(k - i)
                    res = min(res, x)
                last[c].append(k)
            else:
                last[c] = [k]

        return res if res != float("inf") else -1