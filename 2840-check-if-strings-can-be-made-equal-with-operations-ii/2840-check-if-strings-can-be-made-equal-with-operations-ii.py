class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        '''
        if the number of the even c in s1 equal s2
        '''
        n = len(s1)
        s1_odd, s1_even = dict(), dict()
        s2_odd, s2_even = dict(), dict()

        for i in range(n):
            c1 = s1[i]
            c2 = s2[i]
            if i % 2 != 0:
                s1_odd[c1] = s1_odd.get(c1, 0) + 1
                s2_odd[c2] = s2_odd.get(c2, 0) + 1
            else:
                s1_even[c1] = s1_even.get(c1, 0) + 1
                s2_even[c2] = s2_even.get(c2, 0) + 1

        if s1_odd == s2_odd and s1_even == s2_even:
            return True
        
        return False