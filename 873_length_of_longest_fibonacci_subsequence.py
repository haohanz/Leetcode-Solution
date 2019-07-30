# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
from collections import defaultdict
class Solution(object):
    ### Solution 1 - DP
    # DP[i][j]: the max length of subsequence that ends in A[i] and A[j]
    # Time - O(n^2)
    # Space - O(n^2)
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set(A)
        n = len(A)
        D = defaultdict(int)
        for i in xrange(n):
            for j in xrange(i):
                prev = A[i] - A[j]
                if prev < A[j] and prev in s:
                    D[(A[j], A[i])] = D.get((prev, A[j]), 2) + 1
        return max(D.values() or [0])


s = Solution()
assert s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]) == 5
assert s.lenLongestFibSubseq([1,3,7,11,12,14,18]) == 3
assert s.lenLongestFibSubseq([3,7,10]) == 3
assert s.lenLongestFibSubseq([2,5,6,11,13,14,15,17,18,20,22,27,28,31,32,33,38,41,45,46,50,51,55,56,58,61,68,69,73,77,78,84,96,97,107,114,118,122,128,135,151,154,163,166,182,199,206,219,250,263,270,296,321,334,354,404,429,433,478,520,540,573,692,703,774,841,927,1121,1136,1252,1361,1500,1813,1839,2202,2427,2934,2975,3563,3927,4747,4814,5765,6354,7681,7789,9328,10281,12428,12603,15093,16635,20109,20392,24421,26916,32537,39514,52646,63935]) == 18
