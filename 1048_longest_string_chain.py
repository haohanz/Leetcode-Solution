class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # The length of word is O(1)
        # Time: O(nlogn)
        # Space: O(n)
        D = {}
        ret = 0
        for x in sorted(words, key=len):
            new_len = 1
            for i in xrange(len(x)):
                new = x[:i] + x[i+1:]
                if new in D:
                    new_len = max(new_len, D[new] + 1)
            D[x] = new_len
            ret = max(ret, new_len)
        return ret
