"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # S = {}
        # def clone(node):
        #     if node in S: return S[node]
        #     if not node: return None
        #     new = Node(node.val, None, None)
        #     S[node] = new
        #     new.next = clone(node.next)
        #     new.random = clone(node.random)
        #     return new
        # return clone(head)
        
        # build pairs of original node, copied_node.next = node.random, node.random = copied_node
        curr = head
        ret = None
        while curr:
            new = Node(curr.val, None, None)
            if not ret: ret = new
            new.random = curr.random
            curr.random = new
            curr = curr.next

        # build copied list
        curr = head
        while curr:
            copied = curr.random
            tmp = copied.random
            copied.next = tmp.random if tmp else None
            curr = curr.next

        # restore origin
        curr = head
        while curr:
            copied = curr.random
            curr.random = copied.random
            copied.random = copied.next
            copied.next = curr.next.random if curr.next else None
            curr = curr.next
        return ret
