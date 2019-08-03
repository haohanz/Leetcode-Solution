#  https://leetcode.com/problems/regions-cut-by-slashes/
# Solution 1 - Flood Fill
# Time: O(n^2)
# Space: O(n^2)
# Can also solve with union find

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        self.cnt = 0
        n = len(grid)
        M = [[0] * 3 * n for _ in xrange(3 * n)]
        
        def is_bound(i, j):
            return i < 0 or j < 0 or i >= 3*n or j >= 3*n or M[i][j] < 0 or M[i][j] == 1
        
        def dfs(i, j):
            M[i][j] = -1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not is_bound(i + di, j + dj):
                    dfs(i + di, j + dj)
        
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == '\\':
                    M[i * 3][j * 3] = M[i * 3 + 1][j * 3 + 1] = M[i * 3 + 2][j * 3 + 2] = 1
                elif grid[i][j] == '/':
                    M[i * 3 + 2][j * 3] = M[i * 3 + 1][j * 3 + 1] = M[i * 3][j * 3 + 2] = 1
        
        # flood fill
        for i in xrange(3 * n):
            for j in xrange(3 * n):
                if M[i][j] == 0:
                    self.cnt += 1
                    dfs(i, j)
        return self.cnt


