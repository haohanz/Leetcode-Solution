"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        [1 [3[5 6] 2 4]] ==> 1 3 3 2 5 0 6 0 2 0 4 0
        A node value followed by number of children
        :type root: Node
        :rtype: str
        """
        if not root: return ''
        ret = []
        def dfs(node):
            ret.append(node.val)
            ret.append(len(node.children))
            for x in node.children:
                dfs(x)
        dfs(root)
        ret = ' '.join(map(str, ret))
        return ret
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        recursively unpack
        :type data: str
        :rtype: Node
        """
        if not data: return None
        ret = map(int, data.split())
        def dfs(idx):
            if idx >= len(ret):
                return None, idx
            root = Node(ret[idx], [])
            cnt = ret[idx + 1]
            idx += 2
            for i in xrange(cnt):
                child, idx = dfs(idx)
                root.children.append(child)
            return root, idx
        root, idx = dfs(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
