class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        '''
        '''

        def helper(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
            return diff

        res = []
        
        for q in queries:
            for d in dictionary:
                if helper(q, d) <= 2:
                    res.append(q)
                    break
        
        return res
