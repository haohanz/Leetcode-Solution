class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if not node: return
            for x in inorder(node.left): yield x
            yield node.val
            for x in inorder(node.right): yield x

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
