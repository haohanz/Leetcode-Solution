class Solution(object):

    ### Solution 1 - use a stack
    # Time - O(n)
    # Space - O(n)
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ret = 0
        stack = [-1]
        for i, x in enumerate(s):
            if x == ')':
                if len(stack) > 1:
                    stack.pop()
                    ret = max(ret, i - stack[-1])
                else:
                    stack[-1] = i
            elif x == '(':
                stack.append(i)
        return ret
       
    ### Solution 2 - use DP
    # Time - O(n)
    # Space - O(n)
    # DP[i]: the longest length of valid substring that last postion is i
    # Consider end like '....()' and end like '....))'
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        ret = 0
        for i in xrange(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i > 1 else 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 if i - dp[i - 1] - 1 > 0 else dp[i - 1] + 2
                ret = max(ret, dp[i])
        return ret

    ### Solution 3 - save space - two side traverse
    # Time - O(n)
    # Space - O(1)
    # n = len(s)
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        ret = 0
        for i in xrange(n):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l < r:
                l, r = 0, 0
            elif l == r:
                ret = max(ret, 2 * l)
        l, r = 0, 0
        for i in xrange(n - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l > r:
                l, r = 0, 0
            elif l == r:
                ret = max(ret, 2 * l)
        return ret
 
