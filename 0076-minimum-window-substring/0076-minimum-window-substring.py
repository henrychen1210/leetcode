class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = [0] * 52          # 0-25: lowercase, 26-51: uppercase
        window_freq = [0] * 52

        def char_index(c):
            if c.islower():
                return ord(c) - ord('a')
            else:
                return 26 + ord(c) - ord('A')

        def helper(window, need):
            for i in range(52):
                if window[i] < need[i]:
                    return False
            return True

        for c in t:
            freq[char_index(c)] += 1

        left = 0
        res = ""

        for right in range(len(s)):
            window_freq[char_index(s[right])] += 1

            while helper(window_freq, freq):
                if res == "" or right - left + 1 < len(res):
                    res = s[left:right + 1]
                window_freq[char_index(s[left])] -= 1
                left += 1

        return res