"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        copy = {}
        '''

        copy = {}

        def helper(curr):
            if not curr: return

            if curr in copy:
                return copy[curr]

            if curr not in copy:
                copy[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                copy[curr].neighbors.append(helper(nei))
            
            return copy[curr]
        
        return helper(node)
        

