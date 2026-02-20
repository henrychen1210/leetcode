class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        ans = []

        for j in range(len(s)):
            count += 1 if s[j] == '1' else -1
            if count == 0:
                ans.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        
        ans.sort(reverse=True)
    
        return ''.join(ans)