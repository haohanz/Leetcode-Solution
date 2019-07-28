# https://leetcode.com/problems/paint-house-ii/
class Solution(object):
    ### Time: O(nk)
    ### Space: O(1)
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        k, n = len(costs[0]), len(costs)
        min1, min2 = -1, -1
        for i in xrange(n):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            for j in xrange(k):
                if j == last1:
                    costs[i][j] += costs[i-1][last2] if i >= 1 else 0
                else:
                    costs[i][j] += costs[i-1][last1] if i >= 1 else 0
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2, min1 = min1, j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return min(costs[-1])


s = Solution()
assert s.minCostII([[15,17,15,20,7,16,6,10,4,20,7,3,4],[11,3,9,13,7,12,6,7,5,1,7,18,9]]) == 4
