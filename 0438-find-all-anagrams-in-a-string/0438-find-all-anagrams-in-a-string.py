class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        s = "cbaebabacd", p = "abc"
        freq = { a: 1, b: 1, c:1}

        size = 3, {a: 1, b: 1, c: 1}
        left
        0, {a: 1, b: 1, c: 1} V res = [0]
        1, {a: 1, b: 1, e: 1} X


        '''

        p_freq = {}
        win_freq = {}
        size = len(p)
        left = 0
        res = []

        for c in p:
            p_freq[c] = p_freq.get(c, 0) + 1

        need = len(p_freq)
        have = 0

        for c in s[:size]:
            win_freq[c] = win_freq.get(c, 0) + 1
            if win_freq[c] == p_freq.get(c, 0):
                have += 1

        if need == have:
            res.append(left)
        
        while left + size < len(s):
            c = s[left]
            if win_freq[c] == p_freq.get(c, 0):
                have -= 1
            win_freq[c] -= 1

            left += 1
            c = s[left + size - 1]
            win_freq[c] = win_freq.get(c, 0) + 1
            if win_freq[c] == p_freq.get(c, 0):
                have += 1
            
            if need == have:
                res.append(left)
        
        return res