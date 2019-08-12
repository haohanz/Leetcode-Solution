# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ### Solution 1 - 3 passes
    # Time: O(n)
    # Space: O(n)
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ret = [root.val]
        
        def find_left(node):
            if not node: return
            if node.left or node.right:
                ret.append(node.val)
                if node.left:
                    find_left(node.left)
                else:
                    find_left(node.right)
        
        def find_right(node):
            if not node: return
            if node.left or node.right:
                if node.right:
                    find_right(node.right)
                elif node.left:
                    find_right(node.left)
                ret.append(node.val)
            
        def find_leaf(node):
            if not node: return
            if not node.left and not node.right:
                ret.append(node.val)
            if node.left:
                find_leaf(node.left)
            if node.right:
                find_leaf(node.right)
        
        find_left(root.left)
        find_leaf(root.left)
        find_leaf(root.right)
        find_right(root.right)
        return ret


    ### Solution 2 - preorder 1 pass
    # Time: O(n)
    # Space: O(n)
    def boundaryOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        if not root: return []
        
        def preorder(node, lb, rb):
            if not node: return
            if lb: self.ret.append(node.val)
            if not lb and not rb and not node.left and not node.right: self.ret.append(node.val)
            preorder(node.left, lb, rb & (node.right is None))
            preorder(node.right, lb & (node.left is None), rb)
            if (not lb) and rb: self.ret.append(node.val)
        
        self.ret.append(root.val)
        preorder(root.left, True, False)
        preorder(root.right, False, True)
        
        return self.ret

