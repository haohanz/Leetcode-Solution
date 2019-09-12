# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ### recursive solution
    # T(n) = O(logn) + O(logn) + T(n/2) = O((logn)^2)
    # Space: O(logn)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left = right = root
        d = 0
        while left and right: # O(logn)
            d += 1
            left = left.left
            right = right.right
        if not left:
            return (1 << d) - 1
        # at least one of the left and right subtree is a complete tree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    # recursively check if left tree and right tree are complete trees
    # T(n) = O(logn) + T(n/2) = O((logn)^2)
    # Space = O(logn)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(node):
            cnt = 0
            while node:
                node = node.left
                cnt += 1
            return cnt
        
        if not root: return 0
        left = height(root.left)
        right = height(root.right)
        if left == right:
            return (1<<left) + self.countNodes(root.right)
        return (1<<right) + self.countNodes(root.left)
    
        
        
            

