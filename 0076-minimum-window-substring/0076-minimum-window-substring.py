class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Input: s = "ADOBECODEBANC", t = "ABC"
        freq = {A: 1, B: 1, C: 1}

        win_freq = {A: 1}
        [A, B]
        '''
        need = [0] * 52
        window = [0] * 52

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
            need[char_index(c)] += 1

        
        left = 0
        res = ""

        for right in range(len(s)):
            window[char_index(s[right])] += 1
            
            while helper(window, need):
                if res == "" or len(res) > right - left + 1:
                    res = s[left: right + 1]
                window[char_index(s[left])] -= 1
                left += 1

        return res


