from collections import defaultdict

class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        '''
        '''
        n = len(source)
        uf = UF(n)

        for x, y in allowedSwaps:
            uf.union(x, y)
        

        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1
        
        ans = 0

        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                ans += 1
        
        return ans
