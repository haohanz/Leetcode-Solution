# https://leetcode.com/problems/flip-game-ii/
class Solution(object):
    ### Solution 1 - backtrack
    # Time: O(2^n)
    # Space: O(n*2^n)
    def canWinBacktracking(self, s):
        """
        :type s: str
        :rtype: bool
        """
        D = {}
        def backtrack(s):
            if s in D:
                return D[s]
            for i in xrange(len(s) - 1):
                if s[i] == s[i + 1] == '+':
                    if not backtrack(s[:i] + '--' + s[i + 2:]):
                        D[s] = 1
                        return 1
            D[s] = 0
            return 0
        return backtrack(s)

    ### Solution 2 - Sprague-Grundy function
    # Time: O(n^2)
    # Space: O(n)
    # Where n is the max_len of consecutive '+'s
    def canWinSpragueGrundy(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lenth = map(lambda x: len(x), filter(lambda x: len(x) >= 2, s.split('-')))
        if not lenth: return False
        max_len = max(lenth)
        g = [0] * (max_len + 1)
        
        def find_first(max_len, x):
            for i in xrange(max_len + 2):
                if not i in x: return i

        for i in xrange(2, max_len + 1): # O(n) time complexity
            s = set()
            for left_len in xrange(i/2): # O(n) time complexity
                right_len = i - left_len - 2 # get left and right partitioned length
                s.add(g[left_len] ^ g[right_len]) # get all the reachable states
            g[i] = find_first(max_len, s) # find first unreachable value >= 0
        
        # G = g(s_1) ^ g(s_2) ... ^ g(s_k), where s_1 to s_k are subproblems
        return reduce(lambda x, y: x ^ y, map(lambda x: g[x], lenth)) != 0 

