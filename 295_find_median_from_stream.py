# https://leetcode.com/problems/find-median-from-data-stream/
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        small, large = self.heap
        heappush(large, -heappushpop(small, -num))
        if len(small) < len(large):
            heappush(small, -heappop(large))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heap
        if len(small) == len(large):
            return (-small[0] + large[0]) / 2.
        else:
            return -small[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
### Follow up:
# 1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# 2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
# - Use buckets:
#   - If the numbers in the stream are statistically distributed, 
#   then it is easier to keep track of buckets where the median would land, 
#   than the entire array. 
#   Once you know the correct bucket, simply sort it find the median. 
#   If the bucket size is significantly smaller than the size of input processed, 

