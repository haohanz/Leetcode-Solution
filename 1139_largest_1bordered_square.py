# https://leetcode.com/problems/largest-1-bordered-square/
class Solution(object):
    ### Solution 1 - brute force
    # Time - O(n^4)
    # Space - O(1)
    def largest1BorderedSquare0(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        min_len = min(m, n)

        def helper(i, j, l):
            if all(grid[i][j+k] for k in xrange(l)) and \
                all(grid[i+k][j] for k in xrange(l)) and \
                all(grid[i+l-1][j+k] for k in xrange(l)) and \
                all(grid[i+k][j+l-1] for k in xrange(l)):
                return True
            return False

        for l in xrange(min_len, 0, -1): # O(n)
            for i in xrange(m - l + 1): # O(n)
                for j in xrange(n - l + 1): # O(n)
                    if helper(i, j, l): # O(n)
                        return l * l
        return 0

    ### Solution 2 - brute force with ver & hor matrix
    # Time - O(n^3)
    # Space - O(n^2)
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        hor = [[0] * n for _ in xrange(m)]
        ver = [[0] * n for _ in xrange(m)]
        # build hor/ver matrix
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j]:
                    hor[i][j] = hor[i][j-1] + 1 if j > 0 else 1
                    ver[i][j] = ver[i-1][j] + 1 if i > 0 else 1

        def helper(i, j, l):
            return ver[i][j-l+1] >= l and hor[i-l+1][j] >= l

        max = 0
        for i in xrange(m-1, -1, -1): # O(n)
            for j in xrange(n-1, -1, -1): # O(n)
                l = min(ver[i][j], hor[i][j])
                while l > max: # O(n)
                    if helper(i, j, l): max = l # O(1)
                    l -= 1
        return max*max



s = Solution()
assert s.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]) == 9
assert s.largest1BorderedSquare([[1,1,0,0]]) == 1
assert s.largest1BorderedSquare([[0,0,0,0]]) == 0
assert s.largest1BorderedSquare([[0]]) == 0
assert s.largest1BorderedSquare([[1,1],[1,1]]) == 4


