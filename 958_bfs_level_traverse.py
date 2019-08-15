# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        nodes = [root]
        i = 0
        while nodes[i]:
            nodes.append(nodes[i].left)
            nodes.append(nodes[i].right)
            i += 1
        return not any(nodes[i:])
        
    def isCompleteTree2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [(root, 0)]
        i = 0
        while i < len(nodes):
            if nodes[i]:
                nodes.append((nodes[i].left, 2 * i))
                nodes.append((nodes[i].right, 2 * i + 1))
            i += 1
        return nodes[-1][1] == len(nodes)
        

