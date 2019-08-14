class Solution(object):
    ### Solution 1 - Dijkstra
    # always visit the largest value, store in max heap
    # Time: O(mnlog(mn))
    # Space: O(mn)
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
         if not A: return 0
         ret = A[0][0]
         q = [(-A[0][0], 0, 0)]
         D = [(0, 1), (0, -1), (-1, 0), (1, 0)]
         m, n = len(A), len(A[0])

         def is_valid(x,  y):
             return x >= 0 and y >= 0 and x < m and y < n and A[x][y] > 0

         while q:
             val, x, y = heapq.heappop(q)
             A[x][y] = -A[x][y]
             ret = min(ret, -val)
             if x == m - 1 and y == n - 1: return ret
             for dx, dy in D:
                 new_x, new_y = x + dx, y + dy
                 if is_valid(new_x, new_y):
                     heapq.heappush(q, (-A[new_x][new_y], new_x, new_y))

         return 0

    ### Solution 2 - DFS + binary search of target
    # Time = O(nlog(10^9))
    # Space = O(n)
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A: return 0
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(A), len(A[0])
        Seen = set()
        llist = set([])

        # Construct list of targets
        for row in A:
            llist.update([x for x in row if x <= min(A[0][0], A[-1][-1])])
        llist = sorted(list(llist))

        def is_valid(x, y, val):
            return x >= 0 and x < m and y >= 0 and y < n and A[x][y] >= val and (x, y) not in Seen

        def dfs(x, y, val):
            if x == m - 1 and y == n - 1:
                return True
            Seen.add((x, y))
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, val) and dfs(nx, ny, val): return True
            return False

        l, r = 0, len(llist)
        while l < r:
            mid = (l + r) >> 1
            Seen = set()
            # find last valid ==> find first invalid - 1
            if not dfs(0, 0, llist[mid]):
                r = mid
            else:
                l = mid + 1
        return llist[l - 1]
