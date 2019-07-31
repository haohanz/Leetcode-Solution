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
