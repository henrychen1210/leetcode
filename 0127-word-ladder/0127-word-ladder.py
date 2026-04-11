class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        BFS
        beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "lot" | ,"dog",,"log", | "cog"]

        hit
        hot
        dot, lot, 
        dog, log, 
        cog
        '''

        def helper(a, b):
            if len(a) != len(b): return False
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = collections.deque([beginWord])
        visited = set([beginWord])
        res = 0

        while queue:
            n = len(queue)
            res += 1

            for _ in range(n):
                curr = queue.popleft()
                if curr == endWord:
                    return res
                
                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = curr[:i] + c + curr[i+1:]
                        if candidate in wordList and candidate not in visited:
                            queue.append(candidate)
                            visited.add(candidate)
                    

        return 0