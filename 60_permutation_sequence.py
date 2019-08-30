# https://leetcode.com/problems/permutation-sequence/
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # O(n) time
        # O(n) space
        D = [str(i + 1) for i in xrange(n)]
        fact = [1] * n
        for i in xrange(1, n):
            fact[i] = fact[i-1] * (i)
        ret = ''
        k -= 1
        while n:
            div, k = divmod(k, fact[n-1])
            n -= 1
            ret += D[div]
            D.remove(D[div])
        return ret
