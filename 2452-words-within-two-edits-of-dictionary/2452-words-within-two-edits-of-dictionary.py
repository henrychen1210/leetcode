class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.end = False


class Solution:
    def __init__(self):
        self.head = Trie()
    
    def insert(self, s):
        node = self.head
        for c in s:
            idx = ord(c) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Trie()
            node = node.child[idx]
        node.end = True

    def dfs(self, s, idx, node, edits):
        if edits > 2:
            return False
        
        if idx == len(s):
            return node.end
        
        for i in range(26):
            if node.child[i]:
                newEdit = edits + (i != (ord(s[idx]) - ord('a')))
                if self.dfs(s, idx+1, node.child[i], newEdit):
                    return True
        return False


    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        for w in dictionary:
            self.insert(w)
        
        ans= []

        for q in queries:
            if self.dfs(q, 0, self.head, 0):
                ans.append(q)
        
        return ans