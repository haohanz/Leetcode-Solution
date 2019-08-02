# https://leetcode.com/problems/word-pattern/
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        # get index list of first occurance)
        return map(pattern.find, pattern) == map(str.index, str)

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        f = lambda x: map({}.setdefault, x, range(len(x)))
        # get index list of first occurance)
        return f(pattern) == f(str)

