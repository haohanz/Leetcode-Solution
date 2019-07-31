# https://leetcode.com/problems/insert-interval/
class Solution(object):
    def insert(self, intervals, new):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # find last idx nums[idx][1] < interval[0]
        # find first idx nums[idx][1] >= interval[0], l - 1
        # find first idx nums[idx][0] > interval[1]
        n = len(intervals)
        
        def bisect(func):
            l, r = 0, n
            while l < r:
                mid = (l + r) >> 1
                if func(mid):
                    r = mid
                else:
                    l = mid + 1
            return l
        
        start = bisect(lambda x: intervals[x][1] >= new[0]) - 1
        end = bisect(lambda x: intervals[x][0] > new[1])
        if start < n - 1: new[0] = min(new[0], intervals[start + 1][0]) 
        if end > 0: new[1] = max(new[1], intervals[end - 1][1])
        
        return intervals[:start + 1] + [new] + intervals[end:]
        

