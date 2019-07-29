# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
class Solution(object):
    ### Solution 1 - Kruskal: Union Find
    # Space: O(n)
    # Time: O(nlogn)
    def minimumCost_union_find(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        id = range(N + 1)
        size = [1] * (N + 1)

        def union(a, b):
            i, j = root(a), root(b)
            if i == j: return False
            if size[i] < size[j]:
                size[j] += size[i]
                id[i] = j
            else:
                size[i] += size[j]
                id[j] = i
            return True

        def root(a):
            while id[a] != a:
                id[a] = id[id[a]]
                a = id[a]
            return a

        connections = sorted(connections, key=lambda x: x[2])
        ret, edge = 0, 0
        for a, b, l in connections:
            if union(a, b):
                ret, edge = ret + l, edge + 1
        return ret if edge == N - 1 else -1


    ### Solution 2 - Prim: BFS
    # Space: O(n)
    # Time: O(nlogn)
    def minimumCost_bfs(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        from heapq import heappush, heappop
        D = defaultdict(list)
        for a, b, l in connections:
            D[a].append((b, l))
            D[b].append((a, l))

        heap = [[0, 1]]
        seen = set()
        ret, edge = 0, -1
        while heap:
            l, b = heappop(heap)
            if b in seen: continue
            seen.add(b)
            ret, edge = ret + l, edge + 1
            if edge == N - 1: return ret
            for next, next_l in D[b]:
                if not next in seen:
                    heappush(heap, [next_l, next])
        return -1

s = Solution()
assert s.minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]) == 6
assert s.minimumCost(4, [[1,2,3],[3,4,4]]) == -1
