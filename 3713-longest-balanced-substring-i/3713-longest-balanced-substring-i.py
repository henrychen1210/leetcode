class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        for start in range(n):
            count = dict()
            freq = dict()

            for i in range(start, n): 
                c = s[i]

                if c not in count:
                    count[c] = 0

                if count[c] in freq:
                    freq[count[c]].remove(c)

                    if len(freq[count[c]]) == 0:
                        freq.pop(count[c])

                count[c] += 1

                if count[c] not in freq:
                    freq[count[c]] = set()
                freq[count[c]].add(c)

                if len(freq) == 1:
                    res = max(res, i - start + 1)

        return res
                

                