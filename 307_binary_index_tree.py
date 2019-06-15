# 307
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
# Youtube: https://www.youtube.com/watch?v=v_wj_mOAlig

# Not suitable for min/max, sutable for add/multiply/xor
# Build time - O(N)
# Update time - O(logn)
# sumRange time - O(logn)


class NumArray(object):
    def build_tree(self):
        D = [0] + self.nums
        for i in xrange(len(self.nums)):
            D[i+1] += D[i]
        C = [0] * (len(self.nums) +  1)
        for i in xrange(1, len(self.nums) + 1):
            C[i] = D[i] - D[i - (i & -i)]
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

