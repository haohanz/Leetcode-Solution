class ExtendedKMP(object):

    def construct(self, S, T, next=None):
        start, end = 0, 0
        n, m = len(S), len(T)
        extend = [0] * n
        if next is None: # S == T
            next = extend
        for i in xrange(0, n):
            if i >= end or i + next[i - start] >= end:
                if i >= end: end = i # found a match
                while end < n and end - i < m and S[end] == T[end - i]: end += 1
                extend[i] = end - i
                start = i
                if i == 0 and end == n: end = 0 # S == T
            else:
                extend[i] = next[i - start]
        return extend

    def run(self, S, T):
        arr1 = self.construct(T, T)
        arr2 = self.construct(S, T, arr1)
        print 'T:', T, arr1
        print 'S:', S, arr2
        print 'Total number of match is:', len(list(filter(lambda x: x == len(T), arr2)))


kmp = ExtendedKMP()
kmp.run('acacac', 'ac')
kmp.run('aabaaba', 'aababaab')
kmp.run('aacacaccaacca', 'aac')
kmp.run('aaaaabbb', 'aaaaac')
