class Solution(object):
    def isSubSequence(self, str1, str2):
        n, m = len(str1), len(str2)
        i, j = 0, 0
        while i < n and j < m:
            if str1[i] == str2[j]:
                i, j = i + 1, j + 1
            else:
                i += 1
        return j == m
    
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=lambda x: len(x), reverse=True)
        ret = -1
        strs = filter(lambda x: len(x), strs)
        n = len(strs)
        for i in xrange(n):
            flag = True
            for j in xrange(n):
                if i == j: continue
                if self.isSubSequence(strs[j], strs[i]):
                    flag = False
                    break
            if flag:
                ret = max(ret, len(strs[i]))
        return ret

