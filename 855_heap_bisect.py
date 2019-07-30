# https://leetcode.com/problems/exam-room/
### Solution 1 - use heapq [[-dist, x, y]]
### Solution 2 - use bisect (insort) [[dist, -x, y]]

from heapq import *
class ExamRoom(object):

    def __init__(self, N): # O(N)
        """
        :type N: int
        """
        self.N = N
        self.heap = [[- N, -1, N)]

    def get_interval(self, x, y):
        if x == -1:
            dist = y
        elif y == self.N:
            dist = self.N - 1 - x
        else:
            dist = (y - x) / 2
        return (- dist, x, y)

    def seat(self): # O(logN)
        """
        :rtype: int
        """
        (l, x, y) = heappop(self.heap)
        l = -l
        if x == -1: ret = 0
        elif y == self.N: ret = y - 1
        else: ret = x + l
        heappush(self.heap, self.get_interval(x, ret))
        heappush(self.heap, self.get_interval(ret, y))
        return ret

    def leave(self, p): # O(N)
        """
        :type p: int
        :rtype: None
        """
        head, tail = None, None
        for i in xrange(len(self.heap)):
            if self.heap[i][1] == p:
                tail = self.heap[i]
            if self.heap[i][2] == p:
                head = self.heap[i]
            if head and tail: break
        new_interval = self.get_interval(head[1], tail[2])
        self.heap.remove(head)
        self.heap.remove(tail)
        heappush(self.heap, new_interval)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
