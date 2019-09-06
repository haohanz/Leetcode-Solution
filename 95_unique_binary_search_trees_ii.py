# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # Time: nGn
        # Space: nGn
        # Gn: catalan number
        # the number of possible BST is a Catalan number.
        ret = []
        def dfs(remain):
            if not remain: return [None]
            if len(remain) == 1: return [TreeNode(remain[0])]
            ret = []
            for i in xrange(len(remain)):
                left = dfs(remain[:i])
                right = dfs(remain[i+1:])
                for l in left:
                    for r in right:
                        new = TreeNode(remain[i])
                        new.left = l
                        new.right = r
                        ret.append(new)
            return ret
        if n == 0: return []
        return dfs([x + 1 for x in xrange(n)])


