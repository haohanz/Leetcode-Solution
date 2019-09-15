class Solution(object):
    #### sliding window keep minimum
    ## time: O(n)
    ## space: O(n)
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = collections.deque()
        res = A[0]
        pref = 0
        for i in xrange(len(A) * 2):
            x = A[i % len(A)]
            while s and s[0][1] < i - len(A):
                s.popleft()
            pref = pref + x
            res = max(res, pref - s[0][0]) if s else max(res, pref)
            while s and s[-1][0] >= pref:
                s.pop()
            s.append((pref, i))
        return res

    #### kadane's algorithm, one-interval subarrays, or two-interval subarrays.
    # as for two-interval subarrays: max{sum(A) - min(sum(A[i:j]))}
    # time: O(n)
    # space: O(1)
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def helper(gen):
            ans = curr = None
            for x in gen:
                curr = max(curr, 0) + x
                ans = max(ans, curr)
            return ans
        
        ans1 = helper(iter(A))
        # the subarray cannot be empty
        ans2 = sum(A) + helper(-A[i] for i in xrange(1, len(A)))
        ans3 = sum(A) + helper(-A[i] for i in xrange(len(A) - 1))
        return max(ans1, ans2, ans3)

