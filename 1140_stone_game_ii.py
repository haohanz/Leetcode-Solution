# https://leetcode.com/problems/stone-game-ii/
class Solution(object):
    ### Solution 1 - backtrack
    ### Time - O(n^2)
    ### Space - O(n^2)
    def stoneGameII(self, tail):
        """
        :type tail: List[int]
        :rtype: int
        """
        n = len(tail)
        for i in xrange(n - 2, -1, -1):
            tail[i] += tail[i+1]
        D = [[0] * n for _ in xrange(n)]

        def helper(M, idx):
            if idx + 2*M >= n:
                return tail[idx]
            if D[M][idx]: return D[M][idx]
            m = max(tail[idx] - helper(max(M, x-idx), x) for x in xrange(idx + 1, min(n + 1, idx + 2*M + 1)))
            D[M][idx] = m
            return m

        ret = helper(1, 0)
        return ret



s = Solution()
assert s.stoneGameII([2,7,9,4,4]) == 10
assert s.stoneGameII([1,2,3,4,5,100]) == 104
assert s.stoneGameII([2,7,9,4,4,3,6,1,4,1,3,4,1,5,6,1,1]) == 31
