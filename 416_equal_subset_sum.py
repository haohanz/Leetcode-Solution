# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution(object):

    ### Solution 1 - memorization
    # Time = O(2^n)
    # Space = O(2^n)
    def canPartition1(self, nums):
        s = sum(nums)
        n = len(nums)
        if s % 2: return False
        idx_set = set()
        target = s / 2
        self.D = {}
        def helper(arr, target):
            if str(arr) in self.D:
                return self.D[str(arr)]
            n = len(arr)
            if not arr: return False
            if target == 0: return True
            if target < 0: return False
            ret = any(helper(arr[:i] + arr[i + 1:], target - arr[i]) for i in xrange(n))
            self.D[str(arr)] = ret
            return ret

        return helper(nums, target)

    ### Solution 2 - DP
    # Time = O(n) * O(sum/2)
    # Space = O(n) * O(sum/2)
    # dp[i][j]: nums[:i] can have subset with sum equals to j
    # dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
    # i = [0 - n], j = [0 - target]
    def canPartition2(self, nums):
        n = len(nums)
        target = sum(nums)
        if target & 1: return False
        target /= 2
        dp = [[False] * (target + 1) for _ in xrange(n + 1)]
        for i in xrange(len(dp)):
            dp[i][0] = True

        for i in xrange(1, len(dp)):
            for j in xrange(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]

    ### Solution 3 - DP - Space Optimized
    # Time = O(n) * O(sum/2)
    # Space = O(sum/2)
    def canPartition(self, nums):
        target = sum(nums)
        if target & 1: return False
        target /= 2
        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for j in xrange(target, 0, -1):
                if j - x >= 0:
                    dp[j] = dp[j] or dp[j - x]

        return dp[-1]

    ### Solution 4 - use binary to represent all possible subsums for a set
    # Time = O(n) * O(sum/2), constant optimization to Solution 3
    # Space: O(sum) bits
    def canpartition4(self, nums):
        s = 0
        bit = 1 # can sum to 0
        for x in nums:
            s += x
            bit |= bit << x
        return not s & 1 and bit >> (s/2) & 1


s = Solution()
assert s.canPartition([1, 5, 11, 5]) == True
assert s.canPartition([1, 2, 3, 5]) == False
assert s.canPartition([1,2,5]) == False
assert s.canPartition([3,3,3,4,5]) == True
assert s.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]) == True
assert s.canPartition([1, 3, 4, 4]) == False

