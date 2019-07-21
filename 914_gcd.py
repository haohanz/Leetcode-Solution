# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        ### GCD
        # return reduce(fractions.gcd, collections.Counter(deck).values()) > 1
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return reduce(gcd, collections.Counter(deck).values()) > 1

# Related problem: https://leetcode.com/problems/water-and-jug-problem/
