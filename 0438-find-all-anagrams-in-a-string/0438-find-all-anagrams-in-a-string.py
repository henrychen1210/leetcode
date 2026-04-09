class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_freq = {}
        win_freq = {}
        size = len(p)

        for c in p:
            p_freq[c] = p_freq.get(c, 0) + 1
        
        need = len(p_freq)
        have = 0
        left = 0
        res = []

        for i, c in enumerate(s):
            win_freq[c] = win_freq.get(c, 0) + 1
            if win_freq[c] == p_freq.get(c, 0):
                have += 1
            
            if i - left + 1 > size:
                if win_freq[s[left]] == p_freq.get(s[left], 0):
                    have -= 1
                win_freq[s[left]] -= 1
                left += 1
            
            if have == need:
                res.append(left)
        
        return res