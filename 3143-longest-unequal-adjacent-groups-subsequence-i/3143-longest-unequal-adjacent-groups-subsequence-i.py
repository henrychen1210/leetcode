class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        res = []
        lastGroup = 0

        for i in range(n):
            if i == 0 or groups[i] != lastGroup:
                res.append(words[i])
                lastGroup = groups[i]
        
        return res