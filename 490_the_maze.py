# https://leetcode.com/problems/the-maze/
class Solution(object):
    def hasPath(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        def is_boarder(x, y):
            return x == -1 or y == -1 or x == m or y == n or maze[x][y] == 1
        D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        s = [is_boarder(dest[0] + x[0], dest[1] + x[1]) for x in D]
        if s == [1, 1, 0, 0] or s == [0, 0, 1, 1]: return False

        def dfs(x, y):
            if is_boarder(x, y) or maze[x][y] == -1: return False
            if [x, y] == dest: return True
            maze[x][y] = -1
            for dx, dy in D:
                x0, y0 = x + dx, y + dy
                while not is_boarder(x0, y0):
                    x0, y0 = x0 + dx, y0 + dy
                x0, y0 = x0 - dx, y0 - dy
                if dfs(x0, y0):
                    return True
            return False

        return dfs(start[0], start[1])



s = Solution()
assert s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
        [0,4],
        [4,4]) == True
assert s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
        [0,4],
        [1,2]) == True
