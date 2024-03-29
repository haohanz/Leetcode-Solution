# 308: https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = None
            return
        self.matrix = matrix
        m = len(matrix[0])
        n = len(matrix)
        pref = [[0 for _ in xrange(m+1)] for x in xrange(n+1)]
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                pref[i][j] = matrix[i-1][j-1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]
        for j in xrange(m, 0, -1):
            for i in xrange(n, 0, -1):
                pref[i][j] = pref[i][j] + pref[i - (i & -i)][j - (j & -j)] - pref[i - (i & -i)][j] - pref[i][j - (j & -j)]
        self._pref = pref
        self._m = m
        self._n = n

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        if not self.matrix: return
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        row, col = row+1, col+1
        curr_row = row
        while curr_row <= self._n:
            curr_col = col
            while curr_col <= self._m:
                self._pref[curr_row][curr_col] += diff
                curr_col += curr_col & -curr_col
            curr_row += curr_row & -curr_row
    
    def sum(self, row, col):
        ret = 0
        row, col = row+1, col+1
        curr_row, curr_col = row, col
        while curr_row > 0:
            curr_col = col
            while curr_col > 0:
                ret += self._pref[curr_row][curr_col]
                curr_col -= curr_col & -curr_col
            curr_row -= curr_row & -curr_row
        self._pref[curr_row][curr_col]
        return ret
            

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix: return
        return self.sum(row2, col2) + self.sum(row1-1, col1-1) - self.sum(row1-1, col2) - self.sum(row2, col1-1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
