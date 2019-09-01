class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        ### Solution 1 - O(nk) - TLE
        # n = len(nums)
        # if n < 2: return False
        # for i in xrange(n):
        #     for j in xrange(i + 1, min(i + k + 1, n)):
        #         if abs(nums[i] - nums[j]) <= t:
        #             return True
        # return False
        
        ### Solution 2 - binary search - java
        ### Solution 3 - buckets
        # only keep the past k values(indexes)
        if t < 0: return False
        D = {}
        for i, x in enumerate(nums):
            target = x / (t + 1)
            if target in D: return True
            if target - 1 in D and abs(nums[D[target - 1]] - x) <= t: return True
            if target + 1 in D and abs(nums[D[target + 1]] - x) <= t: return True
            D[target] = i
            if i >= k: del D[nums[i - k] / (t + 1)]
        return False

