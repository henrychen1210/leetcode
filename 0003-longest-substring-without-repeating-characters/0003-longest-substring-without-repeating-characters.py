class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        '''

        freq = set()
        left = 0
        res = 0

        for right, c in enumerate(s):
            while c in freq and left <= right:
                freq.remove(s[left])
                left += 1
            freq.add(c)

            res = max(res, right - left + 1)

        return res