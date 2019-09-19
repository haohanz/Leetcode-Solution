class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ### Solution 1 - TLE
        # ret = []
        # wordDict = set(wordDict)
        # self.n = len(s)
        # def dfs(prev, idx):
        #     if idx == self.n:
        #         ret.append(' '.join(prev))
        #         return
        #     if idx > self.n: return
        #     for end in xrange(idx + 1, self.n + 1):
        #         if s[idx: end] in wordDict:
        #             dfs(prev + [s[idx: end]], end)
        # dfs([], 0)
        # return ret
        
        ### Solution 2 - dfs with memorization
        # Time: O(n^3)
        # Space: O(n^3)
        wordDict = set(wordDict)
        self.n = len(s)
        D = {}
        def dfs(idx): # O(n)
            if idx in D: return D[idx]
            ans = []
            if idx == self.n: return [[]]
            if idx > self.n: return []
            for end in xrange(idx + 1, self.n + 1): # O(n)
                if s[idx: end] in wordDict:
                    next = dfs(end)
                    for next_arr in next: # O(n)
                        ans.append(next_arr + [s[idx: end]]) # O(n) space for each list, append O(n) times
            D[idx] = ans
            return D[idx]
        ret = dfs(0)
        return [' '.join(x[::-1]) for x in ret]

