class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # n = len(piles)
        # dp = [[0] * n for _ in xrange(n)]
        # for k in xrange(n):
        #     for i in xrange(n - k):
        #         if k == 0: dp[i][i] = piles[i]
        #         else:
        #             dp[i][i+k] = max(piles[i] - dp[i+1][i+k], piles[i+k] - dp[i][i+k-1])
        # return dp[0][-1] >= 0
        
        # reduce space to O(n)
        n = len(piles)
        dp = piles[:]
        for k in xrange(1, n):
            for i in xrange(n - k):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + k] - dp[i])
        return dp[-1] >= 0
