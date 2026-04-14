class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        freq = {}
        target_freq = {}
        need, have = 0, 0



        '''

        if len(s) < len(t):
            return ""

        target_freq = {}
        freq = {}

        for c in t:
            target_freq[c] = target_freq.get(c, 0) + 1
        
        need, have = len(target_freq), 0

        left = 0
        res = ""

        for right, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            if c in target_freq and freq[c] == target_freq[c]:
                have += 1
            
            while left <= right and have == need:
                if res == "" or len(res) > right - left + 1:
                    res = s[left:right + 1]
                
                left_c = s[left]
                if left_c in target_freq and freq[left_c] == target_freq[left_c]:
                    have -= 1
                freq[left_c] -= 1
                left += 1
        
        return res 