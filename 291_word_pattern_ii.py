class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ### DFS
        # Time: T(n) = T(n-1) + T(n-2) + ... + T(1) = O(2^n), where n = len(str)
        # Space: O(max(26, len(str)))
        # TODO: pushdown automata

        D = {}
        S = set()

        def dfs(pattern_idx, str_idx):
            if pattern_idx == len(pattern) and str_idx == len(str):
                return True
            if pattern_idx == len(pattern) or str_idx == len(str):
                return False
            key = pattern[pattern_idx]
            if key in D:
                start, end = D[key]
                val = str[start: end]
                new_str = str[str_idx: str_idx + end - start]
                if new_str == val and dfs(pattern_idx + 1, str_idx + end - start):
                    return True
                else:
                    return False
            else:
                for end_idx in xrange(str_idx + 1, len(str) + 1):
                    new_str = str[str_idx: end_idx]
                    if new_str in S: continue
                    D[key] = (str_idx, end_idx)
                    S.add(new_str)
                    if dfs(pattern_idx + 1, end_idx): return True
                    del D[key]
                    S.remove(new_str)
            return False
        
        return dfs(0, 0)
