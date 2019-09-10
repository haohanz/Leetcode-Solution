class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        ### DP - top-down
        # DP[l][r][k], the cost of closed range l to r, with k elements following that equal to boxes[r]
        O(n^3) time and space
        n = len(boxes)
        dp = [[[0] * n for _ in xrange(n)] for y in xrange(n)]
        def helper(l, r, k):
            if l > r: return 0
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            if dp[l][r][k] > 0: return dp[l][r][k]
            dp[l][r][k] = helper(l, r - 1, 0) + (k + 1)**2
            for i in xrange(r - 2, l - 1, -1):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], helper(l, i, k + 1) + helper(i + 1, r - 1, 0))
            return dp[l][r][k]
        return helper(0, n - 1, 0)
        
        ### DP - bottom up

