# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre = 0
        self.post = 0

    # Time: O(n)
    # Space: O(n)
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        self.D = {}
        for i, x in enumerate(post):
            self.D[x] = i
        def helper(start, end, start2, end2):
            if start > end or start2 > end2: return None
            root = TreeNode(pre[start])
            if start == end: return root
            left = pre[start + 1]
            pivot = self.D[left]
            left_len = pivot - start2
            root.left = helper(start + 1, start + 1 + left_len, start2, pivot)
            root.right = helper(start + 1 + left_len + 1, end, pivot + 1, end2)
            return root
        return helper(0, len(pre) - 1, 0, len(pre) - 1)
        
    ### solution 2 - recursive with two pointers
    # the tree is counstructed when root.val == post[post_pointer]
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(pre[self.pre])
        self.pre += 1
        if root.val != post[self.post]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[self.post]:
            root.right = self.constructFromPrePost(pre, post)
        self.post += 1
        return root
        
