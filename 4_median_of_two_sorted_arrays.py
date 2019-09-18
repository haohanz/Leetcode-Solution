class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = (m + n) >> 1
        l, r = 0, m
        
        def get_digits(idx):
            a, b = nums1[idx - 1] if idx else float('-inf'), nums1[idx] if idx < m else float('inf')
            idx2 = total - idx
            c, d = nums2[idx2 - 1] if idx2 else float('-inf'), nums2[idx2] if idx2 < n else float('inf')
            return a, b, c, d
        
        def helper(idx):
            a, b, c, d = get_digits(idx)
            if a <= d and c <= b: return 0
            if a < d: return -1
            else: return 1
        
        def result(m, n, idx):
            a, b, c, d = get_digits(idx)
            if (m & 1) == (n & 1):
                return float(max(a, c) + min(b, d)) / 2.
            else:
                return min(b, d)
        
        while l < r:
            mid = (l + r) >> 1
            if helper(mid) >= 0:
                r = mid
            else:
                l = mid + 1
        return result(m, n, l)
