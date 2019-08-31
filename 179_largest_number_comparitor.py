class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x
    
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y): # ret > 0: gt, ret < 0: lt, ret == 0: equal
            if x + y > y + x: return 1
            elif x + y == y + x: return 0
            return -1
        ### Solution 1
        ret = ''.join(sorted(map(str, nums), key=LargerNumKey, reverse=True))
        ### Solution 2
        # ret = ''.join(sorted(map(str, nums), cmp=compare, reverse=True))
        if ret[0] == '0': return '0'
        return ret
