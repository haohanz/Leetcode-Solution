# https://leetcode.com/problems/lfu-cache/

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Solution 1 - use self implemented LinkedList and frequency Dict
Time: O(1) for get and put
Space: O(n)
"""
from collections import defaultdict

class LFUNode(object):
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.start = LFUNode(-1)
        self.end = LFUNode(-1)
        self.start.next = self.end
        self.end.prev = self.start
        self.D = {}

    def size(self):
        return len(self.D)

    def remove(self, key):
        node = self.D[key]
        del self.D[key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def evict(self):
        node = self.start.next
        self.remove(node.key)
        return node.key

    def add(self, key):
        node = LFUNode(key)
        self.end.prev.next = node
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev = node
        self.D[key] = node

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.val = {}
        self.min = -1
        self.D = defaultdict(LinkedList)
        self.N = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.val:
            ret, freq = self.val[key]
            self.val[key] = (ret, freq + 1)
            self.D[freq].remove(key)
            if self.D[freq].size() == 0:
                if freq == self.min:
                    self.min += 1
            self.D[freq + 1].add(key)
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
        if key in self.val:
            self.val[key] = (value, self.val[key][1])
            self.get(key)
            return
        else:
            if len(self.val) == self.N:
                evict_key = self.D[self.min].evict()
                del self.val[evict_key]
            self.min = 1
            self.val[key] = (value, 1)
            self.D[1].add(key)


"""
Solution 2 - use OrderedDict (popitem(last=False)) as LRU cache and frequency Dict
Time: O(1) for get and put
Space: O(n)
"""
from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.val = {}
        self.min = -1
        self.D = defaultdict(OrderedDict)
        self.N = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.val:
            ret, freq = self.val[key]
            self.val[key] = (ret, freq + 1)
            del self.D[freq][key]
            if not self.D[freq]:
                if freq == self.min:
                    self.min += 1
            self.D[freq + 1][key] = 1
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
        if key in self.val:
            self.val[key] = (value, self.val[key][1])
            self.get(key)
        else:
            if len(self.val) == self.N:
                evict_key, _ = self.D[self.min].popitem(last=False) # LRU cache
                del self.val[evict_key]
            self.min = 1
            self.val[key] = (value, 1)
            self.D[1][key] = 1

