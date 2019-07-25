# https://leetcode.com/problems/super-ugly-number/
from heapq import *
class Solution(object):
    ### Solution 1 - DP
    # Time: O(n) * O(k)
    # Space: O(n + k)
    def nthSuperUglyNumberDP(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = [1]
        D = {_: 0 for _ in primes}
        for i in xrange(1, n):
            ugly = min(ret[D[x]] * x for x in primes)
            for x in primes:
                if ugly == ret[D[x]] * x:
                    D[x] += 1
            ret.append(ugly)
        return ret[-1]

    ### Solution 2 - heap
    # Time: O(logk) * O(n)
    # Space: O(n + k)
    # Store the (next_val, idx, prime_val) for boundaries
    def nthSuperUglyNumberHeap(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = [1]
        h = [(x, 0, x) for x in primes]
        heapify(h) # O(klogk)
        for i in xrange(1, n): # O(n)
            ret.append(h[0][0])
            while h[0][0] <= ret[-1]:
                _, idx, prime = heappop(h) # O(logk)
                heappush(h, (ret[idx+1] * prime, idx + 1, prime))
        return ret[-1]

