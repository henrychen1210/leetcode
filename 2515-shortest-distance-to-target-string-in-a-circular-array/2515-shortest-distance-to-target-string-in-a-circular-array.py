class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        '''
        words[(i + 1) % n]
        words[(i - 1 + n) % n]
        '''

        res = n = len(words)
        for i, word in enumerate(words):
            if word == target:
                res = min(res, abs(i - startIndex), n - abs(i - startIndex))
        
        return res if res < n else -1