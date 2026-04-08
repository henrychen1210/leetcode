class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        left, right freq = {}

        s = "abcabcbb"

        res = "", res = s[left:right + 1] if right - left + 1 > len(res)
        left, right, freq
        0, 1, {a: 1}
        0, 2, {a: 1, b: 1}
        0, 3, {a: 1, b: 1, c: 1} res =
        0, 4, {a: 2, b: 1, c: 1} X -> 1, 4, {a: 1, b: 1, c: 1}

        '''

        left = 0
        freq = {}
        res = 0
        dup = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] > 1:
                dup += 1

            while left < right and dup > 0:
                if freq[s[left]] == 2:
                    dup -= 1
                freq[s[left]] -= 1
                left += 1
            
            if dup == 0:
                res = max(res, right - left + 1)
            
        return res
