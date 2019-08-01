# https://leetcode.com/problems/duplicate-zeros/
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if not arr: return
        n = len(arr)
        zero = arr.count(0)
        for i in xrange(n - 1, -1, -1):
            if i + zero < n:
                arr[i + zero] = arr[i]
            if arr[i] == 0:
                zero -= 1
                if arr[i + zero] < n:
                    arr[i + zero] = 0


s = Solution()
s.duplicateZeros([1,0,2,3,0,4,5,0])
s.duplicateZeros([1,0,2,3,0,4,5,0,0])



