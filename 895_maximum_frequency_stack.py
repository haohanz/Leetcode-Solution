# https://leetcode.com/problems/maximum-frequency-stack/
# Time: O(1)
# Space: O(n)
class FreqStack(object):

    def __init__(self):
        self._max = 0
        self._freq = collections.defaultdict(list)
        self._count = collections.defaultdict(int)

    def push(self, x): # O(1)
        """
        :type x: int
        :rtype: None
        """
        freq = self._count[x]
        self._freq[freq + 1].append(x)
        self._count[x] += 1
        self._max = max(self._max, freq + 1)

    def pop(self): # O(1)
        """
        :rtype: int
        """
        ret = self._freq[self._max].pop()
        if not self._freq[self._max]:
            self._max -= 1
        self._count[ret] -= 1
        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
