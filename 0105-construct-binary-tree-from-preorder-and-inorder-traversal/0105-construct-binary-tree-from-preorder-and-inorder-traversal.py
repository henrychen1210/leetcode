# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
         preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

         mid = 1 (3)

        1: mid
        mid + 1: 

        : mid

        mid + 1:
        '''
        inorder_map = { value: index for index, value in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            root = TreeNode(preorder[pre_start])
            mid = inorder_map[preorder[pre_start]]
            left_size = mid - in_start

            root.left = helper(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            root.right = helper(pre_start + left_size + 1, pre_end, mid + 1, in_end)

            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)