class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        ### Solution 1 - dp
        # Time: O(n^2)
        # Space: O(n)
        # dp = [i + 1 for i in xrange(N)]
        # for i in xrange(2, N):
        #     for j in xrange(i - 2):
        #         dp[i] = max(dp[i], dp[j] * (i - j - 1))
        # return dp[-1]
        
        ### Solution 2 - calculate only last few elements for each inner loop
        # Time: O(n)
        # Space: O(1)
        # TODO: prove
        dp = [i + 1 for i in xrange(N)]
        for i in xrange(6, N):
            dp[i] = max(dp[i], dp[i-4]*3, dp[i-5]*4)
        return dp[-1]
