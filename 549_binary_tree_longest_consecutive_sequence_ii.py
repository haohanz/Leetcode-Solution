# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        def dfs(node):
            if not node: return 0, 0
            max_val, min_val = 1, 1
            if node.left:
                max_left, min_left = dfs(node.left)
                if node.left.val == node.val - 1:
                    max_val = max(max_val, max_left + 1)
                if node.left.val == node.val + 1:
                    min_val = max(min_val, min_left + 1)
            if node.right:
                max_right, min_right = dfs(node.right)
                if node.right.val == node.val - 1:
                    max_val = max(max_val, max_right + 1)
                if node.right.val == node.val + 1:
                    min_val = max(min_val, min_right + 1)
            self.ret = max(self.ret, min_val + max_val - 1)
            return max_val, min_val
        dfs(root)
        return self.ret
