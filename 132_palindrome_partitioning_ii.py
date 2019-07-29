class Solution(object):
    # Time: O(n^2)
    # Space: O(n)
    def minCut0(self, s):
        # dp
        n = len(s)
        dp = [[False] * n for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if i == j: dp[i][j] = True
                elif i == j - 1: dp[i][j] = bool(s[i] == s[j])
                else: dp[i][j] = bool(dp[i + 1][j - 1] and s[i] == s[j])

        cut = [n] * n
        cut[0] = 0
        for end in xrange(1, n):
            for start in xrange(end):
                if dp[start][end]:
                    if start > 0:
                        cut[end] = min(cut[end], cut[start - 1] + 1)
                    else:
                        cut[end] = 0
                else:
                    cut[end] = min(cut[end], cut[end - 1] + 1)
        return cut[-1]

    # Time: O(n^2)
    # Space: O(n)
    def minCut(self, s):
        n = len(s)
        cnt = [-1] + range(n)
        for i in xrange(n): # The center of palindrome
            j = 0
            # odd
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                cnt[i + j + 1] = min(cnt[i + j + 1], cnt[i - j] + 1)
                j += 1
            j = 1
            # even
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                cnt[i + j + 1] = min(cnt[i + j + 1], cnt[i - j + 1] + 1)
                j += 1
        print cnt
        return cnt[-1]


s = Solution()
s.minCut("aab")
s.minCut("aba")
s.minCut("abcbaacax")
s.minCut("abcbabcx")
s.minCut("abcde")
