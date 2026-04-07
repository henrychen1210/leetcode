# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        BFS, queue

        [3], []
        [9, 20], [[3]], n = 1
        [15, 7], [[3], [9, 20]],  n = 2
        [], [[3], [9, 20], [15, 7]], n = 2

        res = [[3], [9, 20], [15, 7]]
        '''

        if not root: return []

        queue = deque([root])
        res = []

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return res
        

