# https://leetcode.com/problems/parallel-courses/
from collections import defaultdict, deque
class Solution(object):
    # Solution 1 - bfs
    # Time = O(max(N, len(relations)))
    # Space = O(N)
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        D = defaultdict(list) # graph
        in_degree = [0] * (N + 1) # prerequisite number of each node
        seen = set() # reached node
        queue = deque([]) # bfs queue

        for x, y in relations:
            D[x].append(y)
            in_degree[y] += 1
        for i in xrange(1, N + 1):
            if not in_degree[i]: queue.append(i)
        ret = 0
        while queue:
            l = len(queue)
            ret += 1
            for _ in xrange(l):
                node = queue.popleft()
                seen.add(node)
                child = D[node]
                for x in child:
                    if x in seen: continue
                    in_degree[x] -= 1
                    if not in_degree[x]:
                        queue.append(x)
        return ret if len(seen) == N else -1

s = Solution()
assert s.minimumSemesters(3, [[1,3],[2,3]]) == 2
assert s.minimumSemesters(3, [[1,2],[2,3],[3,1]]) == -1
assert s.minimumSemesters(7, [[2,1],[1,3],[2,3],[1,7],[3,4],[3,5],[3,6],[4,7]]) == 5
assert s.minimumSemesters(7, [[2,1],[1,3],[2,3],[1,7],[3,4],[3,5],[3,6],[4,7],[7,6]]) == 6
