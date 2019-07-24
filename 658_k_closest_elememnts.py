class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            mid = (l + r) >> 1
            # find first idx in [0, n-k], s.t.:
            if x - arr[mid] <= arr[mid + k] - x:
                r = mid
            else:
                l = mid + 1
        return arr[l: l + k]

s = Solution()
assert s.findClosestElements([1,2,3,4,5], 4, 5) == [2,3,4,5]
assert s.findClosestElements([1,2,3,4,5], 4, 0) == [1,2,3,4]
assert s.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4) == [0,1,1,1,2,3,6,7,8]
assert s.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 5) == [1,1,1,2,3,6,7,8,9]

