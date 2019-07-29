# https://leetcode.com/problems/print-zero-even-odd/
from threading import Semaphore
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.curr = 1
        self.a = Semaphore(1)
        self.b = Semaphore(0)
        self.c = Semaphore(0)
	# printNumber(x) outputs "x", where x is an integer.

    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.a.acquire()
            printNumber(0)
            if self.curr & 1:
                self.c.release()
            else:
                self.b.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange(self.n/2):
            self.b.acquire()
            printNumber(self.curr)
            self.curr += 1
            self.a.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange((self.n + 1) >> 1):
            self.c.acquire()
            printNumber(self.curr)
            self.curr += 1
            self.a.release()

