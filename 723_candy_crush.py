# https://leetcode.com/problems/candy-crush/
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        ### Solution 1 - brute force
        # horizonto and vertical, fix with 0, and drop nodes
        flag = True
        m = len(board)
        n = len(board[0])

        while flag:
            # update row and col
            flag = False
            for i in xrange(m):
                for j in xrange(n):
                    val = abs(board[i][j])
                    if val > 0 and j + 2 < n and val == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                        flag = True
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -val
                    if val > 0 and i + 2 < m and val == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                        flag = True
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -val
            # move
            for col in xrange(n):
                idx = m - 1
                for i in xrange(m - 1, -1, -1):
                    if board[i][col] > 0:
                        board[idx][col] = board[i][col]
                        idx -= 1
                for i in xrange(idx, -1, -1):
                    board[i][col] = 0
        return board

s = Solution()
assert s.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]) == [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
assert s.candyCrush([[2,5,5,3,5],[5,4,5,2,3],[2,2,4,5,4],[2,4,4,4,5],[5,2,3,3,5]]) == [[0,0,0,0,5],[0,0,0,3,3],[0,4,5,2,4],[0,2,4,5,5],[5,2,3,3,5]]

