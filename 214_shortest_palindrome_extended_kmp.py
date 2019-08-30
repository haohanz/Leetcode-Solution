class Solution(object):
    def construct(self, S, T, next=None):
        start = end = 0
        n, m = len(S), len(T)
        extend = [0] * n
        if not next: next = extend
        for i in xrange(n):
            if i - start >= m or i + next[i - start] >= end:
                if i >= end: end = i
                while end < n and end - i < m and S[end] == T[end - i]: end += 1
                extend[i] = end - i
                start = i
                if i == 0 and end == n: end = 0
            else:
                extend[i] = next[i - start]
        return extend

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        reverse = s[::-1]
        next = self.construct(s, s)
        extend = self.construct(reverse, s, next)
        idx = 0
        for i, x in enumerate(extend):
            if i + x == len(extend): idx = max(idx, x)
        return s[idx:][::-1] + s


s = Solution()
assert s.shortestPalindrome("aacecaaa") == "aaacecaaa"
assert s.shortestPalindrome("") == ""
assert s.shortestPalindrome("abcd") == "dcbabcd"
assert s.shortestPalindrome("abacd") == "dcabacd"
assert s.shortestPalindrome("aba") == "aba"
assert s.shortestPalindrome("ababbbabbaba") == "ababbabbbababbbabbaba"
