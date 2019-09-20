# https://leetcode.com/problems/lru-cache/
### Solution 1 - use OrderedDict
### Solution 2 - use Double linked list and Dict
# Time: O(1) for get and put
# Space: O(n)

from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.N = capacity
        self.D = OrderedDict()

    def get(self, key, value=None):
        """
        :type key: int
        :rtype: int
        """
        if key in self.D:
            ret = self.D[key]
            del self.D[key]
            self.D[key] = value or ret
            return ret
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.N: return
        if key in self.D:
            self.get(key, value)
        elif len(self.D) == self.N:
            self.D.popitem(last=False)
        self.D[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

### Solution 2 - HashMap + Double Linked List

class LinkedNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n = capacity
        self.dummy = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)
        self.dummy.next = self.tail
        self.tail.prev = self.dummy
        self.D = {}
    
    def _add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def _remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _move_to_last(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.n <= 0 or not key in self.D: return -1
        self._move_to_last(self.D[key])
        return self.D[key].val
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.D:
            self._move_to_last(self.D[key])
            self.D[key].val = value
        else:
            new = LinkedNode(key, value)
            self._add_node(new)
            self.D[key] = new
            if len(self.D) > self.n > 0:
                del self.D[self.dummy.next.key]
                self._remove_node(self.dummy.next)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
