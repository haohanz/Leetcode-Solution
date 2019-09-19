class Solution(object):
    ### Solution 1 - DFS
    # Time: O(n^2)
    # Space: O(n)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordDict = set(wordDict)
        D = [None] * n
        def helper(idx):
            if idx == len(s): return True
            if idx > len(s): return False
            if D[idx] != None: return D[idx]
            D[idx] = False
            for i in xrange(idx + 1, len(s) + 1):
                if s[idx: i] in wordDict and helper(i):
                    D[idx] = True
                    return True
            return False
        return helper(0)
        
        
    ### Solution 2 - bfs
    # Time: O(n^2)
    # Space: O(n)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordDict = set(wordDict)
        visited = [False] * n
        q = collections.deque([0])
        while q:
            x = q.popleft()
            if visited[x]: continue
            for y in xrange(x + 1, n + 1):
                if s[x: y] in wordDict:
                    if y == n: return True
                    q.append(y)
            visited[x] = True
        return False
    
    ### Solution 3 - DP
    # dp[i]: s[:i] can be visited
    # dp[n]: s[:] can be visited
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for end in xrange(1, n + 1):
            for start in xrange(end):
                if dp[start] and s[start: end] in wordDict:
                    dp[end] = True
                    break
        return dp[n]
