class Solution(object):
    ### Solution2 - two passes
    # Time: O(N)
    # Space: O(1)
    def checkValidString0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def run(s, left, right):
            star = 0
            cnt = 0
            for x in s:
                if x == left:
                    cnt += 1
                elif x == right:
                    cnt -= 1
                elif x == '*':
                    star += 1
                if cnt < 0:
                    if abs(cnt) > star:
                        return False
            return True
        if not run(s, '(', ')') or not run(s[::-1], ')', '('): return False
        return True

    ### Solution2 - greedy
    # lo, hi is the smallest and largest number of open left brackets
    # Time: O(N)
    # Space: O(1)
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0
        for x in s:
            lo += 1 if x == '(' else -1
            hi += 1 if x != ')' else -1
            if hi < 0: return False
            if lo < 0: lo = 0
        return lo <= 0

s = Solution()
assert s.checkValidString(')(') == False
assert s.checkValidString('(*)') == True
assert s.checkValidString('(') == False
assert s.checkValidString(')') == False
assert s.checkValidString('((*)(*))((*') == False
assert s.checkValidString('(())((())()()(*)(*()(())())())()()((()())((()))(*') == False
assert s.checkValidString('(*))') == True
