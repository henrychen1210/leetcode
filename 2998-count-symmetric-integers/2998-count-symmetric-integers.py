class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        '''

        '''
        res = 0

        for i in range(low, high + 1):
            
            if len(str(i)) % 2:
                continue

            n = int( len( str( i ) ) / 2 )

            head, tail = 0, 0

            for j in range(0, n):
                head += int(str(i)[j]) 
                tail += int(str(i)[n + j])

            if head == tail:
                res += 1
        
        return res