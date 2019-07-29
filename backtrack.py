# https://leetcode.com/problems/subsets/
# https://leetcode.com/problems/subsets-ii/
# https://leetcode.com/problems/permutations/
# https://leetcode.com/problems/permutations-ii/
# https://leetcode.com/problems/combination-sum/
# https://leetcode.com/problems/combination-sum-ii/
# https://leetcode.com/problems/combination-sum-iii/
# https://leetcode.com/problems/combination-sum-iv/
# https://leetcode.com/problems/palindrome-partitioning/
# https://leetcode.com/problems/palindrome-partitioning-ii/ (see 132, DP)

class Solution(object):
    # Time: O(N!) * O(N)
    # Space: O(N!) * O(N)
    def permute_backtrack(self, nums):
        ret = []
        # res[idx, i] is permuted
        def helper(res, idx):
            if idx == len(res):
                ret.append(res[:])
            for i in xrange(idx, len(res)):
                res[idx], res[i] = res[i], res[idx]
                helper(res, idx + 1)
                res[idx], res[i] = res[i], res[idx]
        helper(nums, 0)
        return ret

    # Time: T(n) = T(n-1) + T(n-2) + ... + T(1) = 2*T(n-1) = O(2^n) * O(n)
    # Space: O(2^n) * O(n)
    def subsets_backtrack():
        ret = []
        def helper(res, idx):
            ret.append(res[:])
            for i in xrange(idx, len(nums)):
                res.append(nums[i])
                helper(res, i + 1)
                res.pop()
        helper([], 0)
        return ret


    # Time: O(2^N) * O(N)
    # Space: O(2^N) * O(N)
    def subsets_bit():
        ret = []
        def helper(i):
            res = []
            for idx in xrange(len(nums)):
                if (1 << idx) & i:
                    res.append(nums[idx])
            ret.append(res)
        for i in xrange(1 << len(nums)): # O(2^n)
            helper(i) #O(n)
        return ret

    # Time: O(2^N) * O(N)
    # Space: O(2^N) * O(N)
    def subsets_duplicate_backtrack():
        nums.sort()
        ret = []
        def helper(res, idx):
            ret.append(res[:])
            for i in xrange(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: continue
                res.append(nums[i])
                helper(res, i + 1)
                res.pop()
        helper([], 0)
        return ret

    # Time: O(N!) * O(N)
    # Space: O(N!) * O(N)
    def permute2_backtrack(self, nums):
        nums.sort()
        ret = []
        used = [0] * len(nums)
        def helper():
            if len(res) == len(nums):
                ret.append(res[:])
                return
            for i in xrange(len(nums)):
                if used[i] or i and nums[i] == nums[i - 1] and not used[i - 1]: continue
                used[i] = 1
                res.append(nums[i])
                helper()
                res.pop()
                used[i] = 0
        res = []
        helper()
        return ret

    # Time: O(N!) * O(N)
    # Space: O(N!) * O(N)
    def permute2_backtrack_counter(self, nums):
        from collections import Counter
        ret = []
        def helper(res, c):
            if len(res) == len(nums):
                ret.append(res[:])
                return
            for x in c:
                if c[x] > 0:
                    c[x] -= 1
                    res.append(x)
                    helper(res, c)
                    res.pop()
                    c[x] += 1
        helper([], Counter(nums))
        return ret

    # Can reuse same element, no duplicate element
    # Time: T(n) = T(n-1) + T(n-2) + ... + T(1) = 2*T(n-1) = O(2^n) * O(n)
    # Space: O(2^n) * O(n)
    def combination_sum(self, nums, target):
        nums.sort()
        ret = []
        self.target = target
        def helper(res, sum, idx):
            if sum == self.target:
                ret.append(res[:])
                return
            if sum > self.target: return
            for i in xrange(idx, len(nums)):
                res.append(nums[i])
                helper(res, sum + nums[i], i) # reuse
                res.pop()
        helper([], 0, 0)
        return ret

    # Cannot reuse same element, has duplicate
    # Time: T(n) = T(n-1) + T(n-2) + ... + T(1) = 2*T(n-1) = O(2^n) * O(n)
    # Space: O(2^n) * O(n)
    def combination_sum2(self, nums, target):
        nums.sort()
        ret = []
        self.target = target
        def helper(res, sum, idx):
            if sum == self.target:
                ret.append(res[:])
                return
            if sum > self.target: return
            for i in xrange(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: continue # skip duplicates
                res.append(nums[i])
                helper(res, sum + nums[i], i + 1)
                res.pop()
        helper([], 0, 0)
        return ret

    # Time: O(n^2) + O(2^n) * O(n)
    # Space: O(2^n) * O(n) + O(n^2)
    def partition(self, s):
        n = len(s)
        # DP, or to save space, can use brute force for a string, same time complexity
        dp = [[0] * n for _ in xrange(n)]
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i, n):
                if i == j:
                    dp[i][j] = 1
                elif i == j - 1:
                    dp[i][j] = int(s[i] == s[j])
                else:
                    dp[i][j] = int(dp[i + 1][j - 1] and s[i] == s[j])

        # backtrack
        # O(2^n) * O(n) time & space
        ret = []
        def helper(res, start):
            if start == n:
                ret.append(res[:])
                return
            for i in xrange(start, n):
                if dp[start][i]:
                    res.append(s[start: i + 1])
                    helper(res, i + 1)
                    res.pop()
        helper([], 0)
        return ret



s = Solution()
print s.permute2([0,0,0,1,9])
