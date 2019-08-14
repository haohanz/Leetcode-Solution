class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        llist = [-1] * (N + 1)
        D = collections.defaultdict(list)
        for x, y in dislikes:
            D[x].append(y)
            D[y].append(x)

        def dfs(node, val):
            if llist[node] != -1:
                return llist[node] == val
            llist[node] = val
            return all(dfs(y, val ^ 1) for y in D[node])

        return all(dfs(node, 1) for node in xrange(1, N + 1) if llist[node] == -1)

