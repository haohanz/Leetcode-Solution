# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
from collections import defaultdict
class Solution(object):
    ### Two pointers
    # Time: O(n)
    # Space: O(1)
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return len(s)
        n = len(s)
        i, j = 0, 0 # close left and close right
        D = defaultdict(int)
        ret = 0
        while i <= j < n:
            D[s[j]] += 1
            if len(D) <= 2:
                ret = max(ret, j - i + 1)
            while i <= j and len(D) > 2:
                D[s[i]] -= 1
                if not D[s[i]]: del D[s[i]]
                i += 1
            j += 1
        return ret


s = Solution()
assert s.lengthOfLongestSubstringTwoDistinct("ccaabbbtftftftfttff23fa0") == 12
assert s.lengthOfLongestSubstringTwoDistinct("eceba") == 3
assert s.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5
