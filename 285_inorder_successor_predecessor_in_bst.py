# https://leetcode.com/problems/inorder-successor-in-bst/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor_iter(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
    
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            return self.inorderSuccessor(root.left, p) or root
    
    def inorderPredecessor(self, root, p):
        if not root: return None
        if root.val >= p.val:
            return self.inorderPredecessor(root.left, p)
        else:
            return self.inorderPredecessor(root.right, p) or root

