# https://leetcode.com/problems/ugly-number-ii/
from heapq import *
class Solution(object):
    ### Solution 1 - heap
    # Time O(nlogn)
    # Space O(n)
    def nthUglyNumber1(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = [1]
        heapify(h)
        s = set()
        for i in xrange(n):
            ret = heappop(h)
            for p in 2, 3, 5:
                if ret * p not in s:
                    heappush(h, ret * p)
                    s.add(ret * p)
        return ret

    ### Solution 2 - DP
    # Time O(n)
    # Space O(n)
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1]
        p2, p3, p5 = 0, 0, 0
        for i in xrange(1, n):
            ugly = min(ret[p2]*2, ret[p3]*3, ret[p5]*5)
            if ugly == ret[p2]* 2:
                p2 += 1
            if ugly == ret[p3]*3:
                p3 += 1
            if ugly == ret[p5]*5:
                p5 += 1
            ret.append(ugly)
        return ret[-1]

s = Solution()
assert s.nthUglyNumber(10) == 12
assert s.nthUglyNumber(1690) == 2123366400
