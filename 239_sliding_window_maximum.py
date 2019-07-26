# https://leetcode.com/problems/sliding-window-maximum/

class Solution(object):
    ### Solution 1 - segment tree
    # Time: O(nlogn)
    # Space: O(n)

    ### Solution 2 - binary search tree
    # Time: O(nlogk)
    # Space: O(n)

    ### Solution 3 - keep a strict onotonic decreasing queue
    # Time: O(n)
    # Space: O(n)
    def maxSlidingWindow3(self, nums, k):
        from collections import deque
        q = deque([]) # store index only, which value decreasing
        n = len(nums)
        ret = []
        for i in xrange(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            while q and q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret

    ### Solution 3 - DP
    # Time: O(n)
    # Space: O(n)
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n == 0: return []
        left = [0] * n
        right = [0] * n
        max_left, max_right = nums[0], nums[-1]
        for i in xrange(n):
            if i % k == 0:
                max_left = nums[i]
            if (n - i) % k == 0:
                max_right = nums[n-i-1]
            max_left = max(max_left, nums[i])
            max_right = max(max_right, nums[n-i-1])
            left[i] = max_left
            right[n-i-1] = max_right
        ret = []
        for i in xrange(n - k + 1):
            ret.append(max(right[i], left[i + k - 1]))
        return ret

s = Solution()
assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
