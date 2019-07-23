# https://leetcode.com/problems/can-i-win/
class Solution(object):
    def canIWin(self, n, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        ### Solution 1 - Time & Space: O(2^20)
        #if desiredTotal <= 0: return True
        #if n * (n + 1) / 2 < desiredTotal: return False

        #self.D = {}
        #def run(s, target):
        #    if s in self.D:
        #        return self.D[s]
        #    start = 1
        #    if target <= 0:
        #        self.D[s] = False
        #        return False
        #    for i in xrange(20):
        #        if s & (start):
        #            x = i + 1
        #            if not run(s - (1 << i), target-x):
        #                self.D[s] = True
        #                return True
        #        start <<= 1
        #    self.D[s] = False
        #    return False

        #t = (1 << n) - 1
        #return run(t, desiredTotal)

        ### Solution 2 - use str(arr)
        if desiredTotal <= 0: return True
        if n * (n + 1) / 2 < desiredTotal: return False

        self.D = {}

        def helper(arr, target):
            if target <= 0: return False
            key = str(arr)
            if key in self.D: return self.D[key]
            for i in xrange(len(arr)):
                if not helper(arr[:i] + arr[i+1:], target - arr[i]):
                    self.D[key] = True
                    return True
            self.D[key] = False
            return False

        return helper(range(1, n+1), desiredTotal)

s = Solution()
assert s.canIWin(12, 16) == True
assert s.canIWin(10, 11) == False
assert s.canIWin(10, 0) == True
assert s.canIWin(2, 16) == False
assert s.canIWin(3, 6) == True
assert s.canIWin(5, 7) == True
assert s.canIWin(12, 128) == False
assert s.canIWin(4, 6) == True
assert s.canIWin(20, 210) == False
assert s.canIWin(19, 190) == True
assert s.canIWin(18, 79) == True
