class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # search for pivot
        if not nums: return -1
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]: l = mid + 1
            else: r = mid
        
        pivot = 0 if l == n else l
        
        def helper(l, r):
            while l < r:
                mid = (l + r) >> 1
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return -1
        
        if target > nums[-1]: return helper(0, pivot)
        else: return helper(pivot, n)
