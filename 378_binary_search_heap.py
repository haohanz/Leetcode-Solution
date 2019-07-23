# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ### Solution 1 - use a heap of size
        ## Time O(mnlogk), space O(k), where matrix is m x n.
        # a = []
        # for i in xrange(len(matrix)):
        #     for j in xrange(len(matrix[0])):
        #         if len(a) < k:
        #             heapq.heappush(a, -matrix[i][j])
        #         else:
        #             heapq.heappushpop(a, -matrix[i][j])
        # return - heapq.heappop(a)

        ### Solution 2 - binary search
        ## Time O(m*logn) * O(log(max-min)), space O(1)

        # Find number of elements <= pivot
        def helper(pivot): # Time: O(m*logn)
            n = len(matrix[0])
            ret = 0
            for row in matrix:
                l, r = 0, n
                while l < r:
                    mid = (l + r) >> 1
                    if row[mid] > pivot: # Find first index that > pivot
                        r = mid
                    else:
                        l = mid + 1
                ret += l
            return ret

        l, r = matrix[0][0], matrix[-1][-1] + 1
        while l < r: # Time: O(log(max-min))
            mid = (l + r) >> 1
            if helper(mid) >= k: # Find first satisfying mid
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
assert s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
assert s.kthSmallest([[-5]], 1) == -5
