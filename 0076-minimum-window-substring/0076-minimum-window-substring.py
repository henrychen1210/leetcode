class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        window_freq = {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        need = len(t_freq)
        have = 0
        left = 0
        res = ""

        for right, c in enumerate(s):
            window_freq[c] = window_freq.get(c, 0) + 1
            if window_freq[c] == t_freq.get(c, 0):
                have += 1
            
            while have == need:
                if res == "" or len(res) > right - left + 1:
                    res = s[left: right + 1]
                
                d = s[left]
                if window_freq[d] == t_freq.get(d, 0):
                    have -= 1
                window_freq[d] -= 1
                left += 1
            
        return res