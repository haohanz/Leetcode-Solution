class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # non shrinking sliding window!
        start = 0
        max_cnt = 0
        D = collections.defaultdict(int)
        for end in xrange(len(s)):
            D[s[end]] += 1
            max_cnt = max(max_cnt, D[s[end]])
            if max_cnt + k < end - start + 1:
                D[s[start]] -= 1
                start += 1
        return len(s) - start
