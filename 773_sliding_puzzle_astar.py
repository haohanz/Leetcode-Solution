class Solution(object):
    ### Solution 1 - BFS
    # Time: O(RC(RC)!)
    # Space: O(RC(RC)!)
    def slidingPuzzleBFS(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.m, self.n = len(board), len(board[0])
        def is_valid(m, n):
            return m >= 0 and n >= 0 and m < self.m and n < self.n

        def swap(board, pos, target):
            board[pos[0]][pos[1]], board[target[0]][target[1]] = board[target[0]][target[1]], board[pos[0]][pos[1]]
        
        terminate = []
        curr = 1
        zero = (0, 0)
        for i in xrange(self.m):
            row = []
            for j in xrange(self.n):
                if board[i][j] == 0:
                    zero = (i, j)
                row.append(curr)
                curr += 1
            terminate.append(row)
        terminate[-1][-1] = 0
        
        q = collections.deque([([row[:] for row in board], zero)])
        level = 0
        visited = set([str(board)])
        Dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            l = len(q)
            for _ in xrange(l):
                board, zero = q.popleft()
                if board == terminate: return level
                for dx, dy in Dir:
                    new_x, new_y = zero[0] + dx, zero[1] + dy
                    if not is_valid(new_x, new_y): continue
                    swap(board, zero, (new_x, new_y))
                    if str(board) not in visited:
                        visited.add(str(board))
                        q.append(([row[:] for row in board], (new_x, new_y)))
                    swap(board, zero, (new_x, new_y))
            level += 1
        return -1

    ### Solution 2 - A Star, a optimazation to Dijkstra
    # Time: less than O(RC(RC)!)
    # Space: O(RC(RC)!)
    def slidingPuzzleAStar(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.m, self.n = len(board), len(board[0])
        Dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def is_valid(m, n):
            return m >= 0 and n >= 0 and m < self.m and n < self.n
        
        def swap(board, pos, target):
            board[pos[0]][pos[1]], board[target[0]][target[1]] = board[target[0]][target[1]], board[pos[0]][pos[1]]
        
        def heuristic(board):
            ret = 0
            for i in xrange(self.m):
                for j in xrange(self.n):
                    val = board[i][j]
                    if val == 0:
                        r, c = self.m - 1, self.n - 1
                    else:
                        r, c = divmod(val - 1, self.n)
                    ret += abs(i - r) + abs(c - j)
            return ret
        
        terminate = []
        curr = 1
        zero = (0, 0)
        for i in xrange(self.m):
            row = []
            for j in xrange(self.n):
                if board[i][j] == 0:
                    zero = (i, j)
                row.append(curr)
                curr += 1
            terminate.append(row)
        terminate[-1][-1] = 0

        h = heuristic(board)
        D = {str(board): h}
        heap = [(h, 0, [row[:] for row in board], zero)]
        
        while heap:
            cost, g, board, zero = heapq.heappop(heap)
            if board == terminate: return g
            if str(board) in D and cost != D[str(board)]: continue
            for dx, dy in Dir:
                new_x, new_y = zero[0] + dx, zero[1] + dy
                if is_valid(new_x, new_y):
                    swap(board, zero, (new_x, new_y))
                    cost = heuristic(board) + g + 1
                    if str(board) not in D or D[str(board)] > cost:
                        D[str(board)] = cost
                        heapq.heappush(heap, (cost, g + 1, [row[:] for row in board], (new_x, new_y)))
                    swap(board, zero, (new_x, new_y))
        return -1

