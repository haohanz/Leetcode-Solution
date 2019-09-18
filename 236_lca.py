# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ret = None
        def dfs(node):
            if not node: return False
            l = dfs(node.left)
            r = dfs(node.right)
            z = node == p or node == q
            if l + r + z >= 2:
                self.ret = node
            return l or r or z
        dfs(root)
        return self.ret

