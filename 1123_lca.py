# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ### Return the level instead of height, to make sure always update on the deepest nodes
        self.ret, self.level = None, 0
        def dfs(node, level):
            if not node: return level - 1
            self.level = max(self.level, level)
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            if left == right == self.level:
                self.ret = node
            return max(left, right)
        dfs(root, 0)
        return self.ret

