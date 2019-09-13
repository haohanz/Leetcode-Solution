# 307
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
# Youtube: https://www.youtube.com/watch?v=v_wj_mOAlig

# Not suitable for min/max, sutable for add/multiply/xor
# Build time - O(N)
# Update time - O(logn)
# sumRange time - O(logn)
# Cannot solve min/max task, because min(a, b) cannot be solved with min(a[i:j]) = sum(a[j]) - sum(a[i])
# But can solve multiply, xor, max

class NumArray(object):
    def build_tree(self):
        C = [0] + self.nums
        for i in xrange(len(self.nums)):
            C[i+1] += C[i]
        for i in xrange(len(self.nums), 0, -1):
            C[i] -= C[i - (i & -i)]
        self.C = C

    def __init__(self, nums):
        self.nums = nums
        self.build_tree()

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= len(self.nums):
            self.C[i] += diff
            i += i & -i

    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.C[i]
            i -= i & -i
        return ret

    def sumRange(self, i, j):
        return self.sum(j) - self.sum(i-1)

