class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def get_path(node, target, path):
            if not node:
                return False
            path.append(node)
            if node.val == target.val:
                return True
            if get_path(node.left, target, path) or get_path(node.right, target, path):
                return True
            path.pop()  # backtrack
            return False

        path1, path2 = [], []
        get_path(root, p, path1)
        get_path(root, q, path2)

        # Find last common node
        lca = root
        for n1, n2 in zip(path1, path2):
            if n1.val == n2.val:
                lca = n1
            else:
                break
        return lca