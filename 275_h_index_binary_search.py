# https://leetcode.com/problems/h-index-ii/
# https://leetcode.com/problems/h-index/
# A scientist has index h if h of his/her N papers have at least h citations each,
# and the other N − h papers have no more than h citations each.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
	### When citations is sorted
        # Reference (figure): https://leetcode.com/problems/h-index/solution/
        # Find last index i, s.t. n - i - 1 >= citations[i], return n - i
        # i.e. Find first index i, s.t. n - i - 1 < citations[i], return n - i + 1
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = (l + r) >> 1
            if n - mid - 1 < citations[mid]:
                r = mid
            else:
                l = mid + 1
        return n - l

    def hIndex2(self, citations):
        ### If not sorted
        ### Solution 1: sort -> hIndex, Time O(nlogn) + O(logn), Space O(1)
        ### Solution 2: buckets, Time O(n), Space O(n)
        n = len(citations)
        bucket = [0] * (n + 1)
        for x in citations:
            bucket[min(x, n)] += 1
        sum = 0
        for i in xrange(n, 0, -1):
            sum += bucket[i]
            # Inversily, find first index i, s.t. num_paper >= i
            if not sum >= i:
                continue
            else:
                return i
        return 0


s = Solution()
assert s.hIndex([0,1,3,5,6]) == 3
assert s.hIndex([0,1,3,5,6,7]) == 3
assert s.hIndex([0,1,3,5,6,7,8]) == 4
assert s.hIndex([0,0]) == 0
assert s.hIndex([10]) == 1
assert s.hIndex([1]) == 1
assert s.hIndex([2]) == 1
assert s.hIndex([11,15]) == 2
