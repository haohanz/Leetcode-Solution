# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# https://leetcode.com/problems/partition-equal-subset-sum/
# Given an array of integers 
# nums and a positive integer k, 
# find whether it's possible to divide this array into k 
# non-empty subsets whose sums are all equal.


class Solution(object):
    def canPartitionKSubsetsRecursive(self, nums, k):
        visited = [False] * len(nums)

        def canPartition(nums, curr_sum, start_idx, curr_num, target, k):
            if k == 1: return True
            if curr_sum == target and curr_num > 0: return canPartition(nums, 0, 0, 0, target, k - 1)
            if curr_sum > target: return False
            for i in xrange(start_idx, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if canPartition(nums, curr_sum + nums[i], i + 1, curr_num + 1, target, k): return True
                    visited[i] = False
            return False

        s = sum(nums)
        if s % k: return False
        return canPartition(nums, 0, 0, 0, s/k, k)

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k: return False
        self.sub_sum = sum(nums) / k
        if max(nums) > self.sub_sum: return False
        n = len(nums)
        m = 1 << n
        dp = [0] * m
        for i in xrange(m): # O(2^n)
            ret = 0
            for j in xrange(n): # O(n)
                if i & (1<<j):
                    ret += nums[j]
            dp[i] = ret

        def helper(used, start, k):
            if k == 0: return True
            for i in xrange(start, len(dp)): # O(2^n)
                x = dp[i]
                if x == self.sub_sum and i & used == 0:
                    # no need to search previous ones: all ready searched
                    if helper(i | used, i + 1, k - 1):
                        return True
            return False

        return helper(0, 0, k)


s = Solution()
assert s.canPartitionKSubsets([4,3,2,3,5,2,1], 4) == True
assert s.canPartitionKSubsets([1,2,3,1,2], 3) == True
assert s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3) == True
assert s.canPartitionKSubsets([2957,4566,1740,1691,594,804,970,327,1473,4163,1097,8564,1633,1577,1944,1464], 4) == True
assert s.canPartitionKSubsets([605,454,322,218,8,19,651,2220,175,710,2666,350,252,2264,327,1843], 4) == True
