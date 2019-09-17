class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ### Solution 1 - DP
        ## Time: O(n**2)
        ## Space: O(n**2)
        # dp[i][j]: i to j is palindrome or not
        # dp[i][j] = dp[i+1][j-1] + 2 if i == j
        # n = len(s)
        # dp = [[0] * n for _ in xrange(n)]
        # # dp[i][i] = 1
        # for i in xrange(n): dp[i][i] = 1
        # longest = None
        # ret = (0, 0)
        # for k in xrange(1, n):
        #     for i in xrange(n):
        #         if i + k >= n: break
        #         if k == 1: dp[i][i+k] = 2 if s[i] == s[i+k] else 0
        #         else: dp[i][i+k] = dp[i+1][i+k-1] + 2 if s[i] == s[i+k] and dp[i+1][i+k-1] != 0 else 0
        #         longest = max(longest, dp[i][i+k])
        #         if dp[i][i+k] == longest != 0:
        #             ret = (i, i + k)
        # return s[ret[0]: ret[1] + 1]
        
        ### Solution 2 - use expand center - 2n-1 centers in total, expansion use O(n) time
        ## Time: O(n**2)
        ## Space: O(1)
        def expand(nums, center):
            if center & 1: # odd
                l, r = (center-1) / 2, (center + 1) / 2
            else:
                l, r = (center - 2) / 2, (center + 2) / 2
            while l >= 0 and r < len(nums) and nums[l] == nums[r]:
                l, r = l - 1, r + 1
            return l + 1, r - 1, r - l - 1
    
        n = len(s)
        max_len = None
        ret = (0, 0)
        for i in xrange(2*n - 1):
            l, r, length = expand(s, i)
            if length > max_len:
                max_len = length
                ret = (l, r)
        return s[ret[0]: ret[1] + 1]

