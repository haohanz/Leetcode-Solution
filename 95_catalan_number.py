# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


### Time: T(n) = T(1)*T(n-2) + T(2) * T(n-3) + ... + T(n-2)*T(1) + T(n-1) * T(0) = Catalan number
### Space: Catalan number
### Details: https://leetcode.com/articles/unique-binary-search-trees/
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        D = {}
        def run(start, end):
            if (start, end) in D: return D[(start, end)]
            if start > end: return [None]
            ret = []
            for i in xrange(start, end + 1):
                l_list = run(start, i - 1)
                r_list = run(i + 1, end)
                for l in l_list:
                    for r in r_list:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ret.append(root)
            D[(start, end)] = ret
            return ret
        
        return filter(lambda x: x is not None, run(1, n))

