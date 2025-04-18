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
        pair = []
        pre, count = s[0], 0
        res = ""

        for i in range(1, n):
            if pre == s[i]:
                count += 1
            else:
                pair.append([count + 1, int(pre)])
                pre = s[i]
                count = 0
            
        pair.append([count + 1, int(pre)])

        for i in range(len(pair)):
            res += str(pair[i][0]) + str(pair[i][1])

        return res