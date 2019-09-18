# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ### solution 1 - recursive
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
        
    ### solution 2 - iterative
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        while stack and (not p in parent or not q in parent):
            x = stack.pop()
            if x.left:
                parent[x.left] = x
                stack.append(x.left)
            if x.right:
                parent[x.right] = x
                stack.append(x.right)
        parents = set()
        while p:
            parents.add(p)
            p = parent[p]
        while not q in parents:
            q = parent[q]
        return q

