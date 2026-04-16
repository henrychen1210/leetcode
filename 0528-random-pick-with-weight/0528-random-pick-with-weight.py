import random
class Solution:
    '''
    [1, 3]
    0 <-> 3 
    0 -> 0
    1 - 3 -> 1

    {
        1: 0,
        4: 1
    }
    '''

    def __init__(self, w: List[int]):
        self.pool = {}
        
        idx = 0
        for i, n in enumerate(w):
            idx += n
            self.pool[idx] = i

        self.idx = idx


    def pickIndex(self) -> int:
        pick = random.randrange(0, self.idx)

        for k, v in self.pool.items():
            if k > pick:
                return v
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()