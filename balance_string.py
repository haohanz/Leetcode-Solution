'''
A balanced string is a string constructed by '0' and '1', which doesn't have 3 same & consecutive characters.
E.g. balanced string with length (n) = 3: 001, 010, 011, 100, 101, 110. 6 strings in total.
'''
class Solution(object):
    '''
    Output all the balanced string given n
    '''
    def get_balance_string(self, n):
        ret = []
        def dfs(prev):
            if len(prev) >= 3 and prev[-1] == prev[-2] == prev[-3]: return
            if len(prev) == n:
                ret.append(prev)
                return
            dfs(prev + '1')
            dfs(prev + '0')
        dfs('')
        print ret
        print len(ret)
        return ret

    '''
    Output the number of balanced string given n
    dp0[i] = dp1[i-1] + dp1[i-2]
    dp1[i] = dp0[i-1] + dp0[i-2]
    dp0[0], dp1[0] = 1
    dp0[1], dp1[1] = 2
    Time: O(n)
    Space: O(1)
    '''
    def count_balance_string(self, n):
        dp = [1, 2, 0]
        for i in xrange(1, n - 1):
            dp[(i + 1) % 3] = dp[i % 3] + dp[(i - 1) % 3]
        ret = dp[(n - 1) % 3] * 2
        print ret
        return ret

    '''
    Output the number of balanced string given n
    Use fibonacci generator
    Time: O(n)
    Space: O(1)
    '''
    def count_balance_string_generator(self, n):
        def fibonacci(n):
            a, b = 1, 2
            for i in xrange(n):
                yield a
                a, b = b, a + b
        f = fibonacci(n)
        for x in f:
            ret = x * 2
        print ret
        return ret

    '''
    Output the number of balanced string given n
    Use fibonacci closed form https://en.wikipedia.org/wiki/Fibonacci_number
    Time: O(1)
    Space: O(1)
    '''
    def count_balance_string_closed_form(self, n):
        from math import sqrt
        fai = (1 + sqrt(5)) / 2.
        numerator = fai ** (n + 1) - (1 - fai) ** (n + 1)
        denominator = sqrt(5)
        ret = int(numerator / denominator) * 2
        print ret
        return ret


s = Solution()
s.get_balance_string(7)
s.count_balance_string_closed_form(7)
