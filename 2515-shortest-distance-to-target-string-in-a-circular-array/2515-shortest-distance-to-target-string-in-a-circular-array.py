class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        '''
        words[(i + 1) % n]
        words[(i - 1 + n) % n]
        '''

        if words[startIndex] == target:
            return 0

        n = len(words)
        res = float('inf')
        
        # right
        curr = (startIndex + 1) % n
        step = 1
        while curr != startIndex:
            print(curr)
            if words[curr] == target:
                res = min(res, step)
                break
            else:
                curr = (curr + 1) % n
                step += 1


        # left
        curr = (startIndex - 1 + n) % n
        step = 1
        while curr != startIndex:
            if words[curr] == target:
                res = min(res, step)
                break
            else:
                curr = (curr - 1 + n) % n
                step += 1

        return res if res != float('inf') else -1