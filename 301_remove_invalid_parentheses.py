class Solution(object):
    ### Solution 1 - brute force
    # Time: O(2^n) ~ O(n*2^n)
    # Space: O(n)
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        level = {s}
        def is_valid(str):
            cnt = 0
            for x in str:
                if x == '(': cnt += 1
                elif x == ')': cnt -= 1
                if cnt < 0: return False
            return cnt == 0
        while level:
            ret = filter(is_valid, level)
            if ret: return ret
            level = {s[:i] + s[i+1:] for s in level for i in xrange(len(s))}

    ### Solution 2 - recursive run from left and right
    # Time: worst case O(2^n), when s == '))))))))'
    # Space: O(n^2) stack space
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def run(s, start, last, left='(', right=')'):
            cnt = 0
            for i in xrange(start, len(s)):
                if s[i] == left:
                    cnt += 1
                elif s[i] == right:
                    cnt -= 1
                if cnt < 0:
                    for j in xrange(last, i + 1):
                        if s[j] == right and (j == last or s[j] != s[j-1]):
                            run(s[:j] + s[j+1:], i, j, left, right)
                    return
            reverse = s[::-1]
            if left == '(':
                run(reverse, 0, 0, right, left)
            else:
                res.append(reverse)
        run(s, 0, 0)
        return res

    ### Solution 3 - simple backtrack
    # Time: O(2^n)
    # Space: O(n)
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set([''])
        self.max_len = 0
        def backtrack(idx, prev, cnt):
            if idx == len(s):
                if cnt == 0 and len(prev) >= self.max_len:
                    res.add(''.join(prev))
                    self.max_len = max(self.max_len, len(prev))
                return
            if cnt < 0: return
            ch = s[idx]
            if ch in '()':
                backtrack(idx + 1, prev, cnt)
            if ch == '(':
                cnt += 1
            elif ch == ')':
                cnt -= 1
            prev.append(ch)
            backtrack(idx + 1, prev, cnt)
            prev.pop()

        backtrack(0, [], 0)
        res = filter(lambda x: len(x) >= self.max_len, res)
        return res

