# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder = [3, 9, 20, 15, 7] root -> left -> right
        inorder = [9, 3, 15, 20, 7] left -> root -> right

        mid = 1 (3)
        '''

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        left_preorder = preorder[1: mid + 1]
        right_preorder = preorder[mid + 1:]
        left_inorder = inorder[: mid]
        right_inorder = inorder[mid  + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

