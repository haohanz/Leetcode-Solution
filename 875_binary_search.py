# https://leetcode.com/problems/koko-eating-bananas/
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        if len(piles) == H:
            return max(piles)
        l, r = 1, max(piles) + 1
        while l < r:
            mid = (l + r) >> 1
            ret = sum(- ( -x / mid) for x in piles)
            if H >= ret:
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
assert s.minEatingSpeed([30,11,23,4,20], 6) == 23
assert s.minEatingSpeed([312884470], 968709470) == 1

