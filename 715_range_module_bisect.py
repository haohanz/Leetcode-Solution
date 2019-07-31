# https://leetcode.com/problems/range-module/
class RangeModuleSolution1(object):

    def __init__(self):
        self.arr = []

    def bisect(self, func):
        l, r = 0, len(self.arr)
        while l < r:
            mid = (l + r) >> 1
            if func(mid): r = mid
            else: l = mid + 1
        return l
    
    def findBoundary(self, left, right):
        # find last idx: idx[1] < left
        # find first idx: idx[1] >= left, idx -= 1
        start = self.bisect(lambda x: self.arr[x][1] >= left) - 1
        # find first idx: idx[0] > right
        end = self.bisect(lambda x: self.arr[x][0] > right)
        return start, end
        
    def addRange(self, left, right): # O(1000)
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        if not self.arr:
            self.arr = [[left, right]]
            return
        start, end = self.findBoundary(left, right)
        if start < len(self.arr) - 1:
            left = min(left, self.arr[start + 1][0])
        if end > 0:
            right = max(right, self.arr[end - 1][1])
        self.arr = self.arr[: start + 1] + [[left, right]] + self.arr[end:]

        
    def queryRange(self, left, right): # O(log(1000))
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        # bisect
        start, end = self.findBoundary(left, right)
        return start == end - 2 and self.arr[start + 1][0] <= left and self.arr[start + 1][1] >= right
        

    def removeRange(self, left, right): # O(1000)
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        start, end = self.findBoundary(left, right)
        ret = []
        if start < len(self.arr) - 1 and self.arr[start + 1][0] < left:
            ret.append([self.arr[start + 1][0], left])
        if end > 0 and self.arr[end - 1][1] > right:
            ret.append([right, self.arr[end - 1][1]])
        self.arr = self.arr[: start + 1] + ret + self.arr[end:]
        
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

from bisect import bisect_left as bl, bisect_right as br
class RangeModuleSolution2(object):

    def __init__(self):
        self._arr = []

    def addRange(self, left, right): # O(1000)
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        start, end = bl(self._arr, left), br(self._arr, right)
        self._arr[start: end] = [left] * (start & 1 == 0) + [right] * (end & 1 == 0)

    def queryRange(self, left, right): # O(log(1000))
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        start, end = br(self._arr, left), bl(self._arr, right)
        return start == end and start & 1 == 1

    def removeRange(self, left, right): # O(1000)
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        start, end = bl(self._arr, left), br(self._arr, right)
        self._arr[start: end] = [left] * (start & 1 == 1) + [right] * (end & 1 == 1)
