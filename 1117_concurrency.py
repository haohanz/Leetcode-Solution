# https://leetcode.com/problems/building-h2o/
from threading import Lock

class H2O(object):
    def __init__(self):
        self.H = 0
        self.O = 0
        self.lock = Lock()


    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.releaseH = releaseHydrogen
        with self.lock:
            self.H += 1
            self.start()

    def oxygen(self, releaseHydrogen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.releaseO = releaseHydrogen
        with self.lock:
            self.O += 1
            self.start()

    def start(self):
        while self.ok():
            self.releaseH()
            self.releaseH()
            self.releaseO()
            self.H -= 2
            self.O -= 1

    def ok(self):
        return self.H >= 2 and self.O >= 1
