class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        '''
        '''

        res = 0
        count = 0

        for m in moves:
            if m == 'R':
                res += 1
            elif m == 'L':
                res -= 1
            else:
                count += 1
        
        return max(abs(res + count), abs(res - count))