class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # cnt means how many letters are remained unvisited
        D = collections.Counter(t)
        n, cnt = len(s), len(t)
        i, j, min_len = 0, 0, n + 1
        ret = ''
        while j < n:
            while j < n and cnt: # invalid
                D[s[j]] -= 1
                if D[s[j]] >= 0: cnt -= 1
                j += 1
            while i < j and cnt == 0: # valid
                if j - i < min_len:
                    min_len = j - i
                    ret = s[i: j]
                D[s[i]] += 1
                if D[s[i]] == 1: cnt += 1
                i += 1
        return '' if min_len == n + 1 else ret

