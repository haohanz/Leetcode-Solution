class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(x):
            if not x % 2 or x < 2: return x == 2 
            for i in xrange(3, int(math.sqrt(x)) + 1, 2):
                if not x % i:
                    return False
            return True

        if N <= 11 and N >= 8: return 11
        for x in xrange(10 ** (len(str(N)) / 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and is_prime(y):
                return y

