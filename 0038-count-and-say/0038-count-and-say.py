class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        '''
        if n == 1:
            return "1"
        else:
            return self.helper(self.countAndSay(n - 1))

    def helper(self, s):
        n = len(s)
        pre, count = s[0], 0
        res = ""

        for i in range(1, n):
            if pre == s[i]:
                count += 1
            else:
                res += str(count + 1) + str(pre)
                pre = s[i]
                count = 0
            
        res += str(count + 1) + str(pre)

        return res