class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        '''

        '''
        res = 0

        for i in range(low, high + 1):
            if i < 100 and i % 11 == 0:
                res += 1
                continue
            if 1000 < i < 10000:
                head = i // 1000 + i % 1000 // 100
                tail = i % 10 + i % 100 // 10
                if head == tail:
                    res += 1
        
        return res