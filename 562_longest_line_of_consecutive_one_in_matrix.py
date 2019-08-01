# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
### Solution 1 - 4 pass traverse
### Solution 2 - use DP
# Time: O(mn)
# Space: O(mn)
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        m = len(M)
        n = len(M[0])
        DP = [[(0, 0, 0, 0)] * (n + 2) for _ in xrange(m + 1)]
        ret = 0
        for i in xrange(m):
            for j in xrange(n):
                if M[i][j]:
                    DP[i + 1][j + 1] = (DP[i + 1][j][0] + 1, DP[i][j + 1][1] + 1, DP[i][j][2] + 1, DP[i][j + 2][3] + 1)
                    ret = max(ret, max(DP[i + 1][j + 1]))
        return ret

