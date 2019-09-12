class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

   def findMidDuplicate(self, nums):
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]
