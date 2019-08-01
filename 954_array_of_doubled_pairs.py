# https://leetcode.com/problems/array-of-doubled-pairs/
from collections import Counter
from collections import defaultdict
from math import log
class Solution(object):
    ### Solution 1 - count & sorting
    # Time: O(nlogn)
    # Space: O(n)
    def canReorderDoubled1(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        c = Counter(A)
        for x in sorted(A, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True

    ### Solution 2 - two pointer
    # Time: O(n)
    # Space: O(1)
    def canReorderDoubled2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort(key=lambda x: (x < 0, abs(x)))
        j, dummy = 1, 100000
        n = len(A)
        for i in xrange(n):
            if A[i] == dummy: continue
            if j <= i: j = i + 1
            while j < n and (A[j] != A[i] * 2 or A[j] == dummy):
                j += 1
            if j >= n: return False
            A[j] = dummy
        return True

    ### Solution 3 - bucket sort, idx = last position of 1
    # Time: O(n)
    # Space: O(n)
    def canReorderDoubled3(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        bucket = [defaultdict(int) for _ in xrange(32)]
        if A.count(0) & 1: return False
        for n in A:
            if n: bucket[int(log((n & -n), 2))][n] += 1
        for i in xrange(31):
            for n in bucket[i]:
                if bucket[i + 1][n * 2] < bucket[i][n]:
                    return False
                bucket[i + 1][n * 2] -= bucket[i][n]
        return True

s = Solution()
assert s.canReorderDoubled1([1,2,1,-8,8,-4,4,-4,2,-2]) == True
assert s.canReorderDoubled1([-8,-4,-2,-1,0,0,1,2,4,8]) == True
assert s.canReorderDoubled1([0,4,-4,-3,-3,8,-3,-6,-4,-6,-6,-4,-8,-4,-8,0]) == False

