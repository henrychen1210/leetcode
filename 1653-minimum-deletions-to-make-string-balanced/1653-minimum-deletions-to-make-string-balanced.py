class Solution:
    def minimumDeletions(self, s: str) -> int:
        '''
        '''
        n = len(s)
        b_prefix = [0] * n # how many 'b' before 'a'
        a_sufix = [0] * n # how many 'a' after 'b'
        reversed_s = s[::-1]
        count_a, count_b = 0, 0

        for i in range(len(s)):
            b_prefix[i] = count_b
            if s[i] == "b":
                count_b += 1
            
            a_sufix[i] = count_a
            if reversed_s[i] == "a":
                count_a += 1
        
        a_sufix = a_sufix[::-1]

        res = n
        for i in range(n):
            res = min(res, b_prefix[i] + a_sufix[i])
        
        return res
