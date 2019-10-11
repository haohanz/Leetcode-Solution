class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        m, n = len(S), len(T)
        ptr1, ptr2 = m - 1, n - 1
        cnt1, cnt2 = 0, 0
        while True:
            while ptr1 >= 0 and (S[ptr1] == '#' or cnt1):
                cnt1 += 1 if S[ptr1] == '#' else -1
                ptr1 -= 1
            while ptr2 >= 0 and (T[ptr2] == '#' or cnt2):
                cnt2 += 1 if T[ptr2] == '#' else -1
                ptr2 -= 1
            if not (ptr1 >= 0 and ptr2 >= 0 and S[ptr1] == T[ptr2]):
                return ptr1 == ptr2 == -1
            ptr1, ptr2 = ptr1 - 1, ptr2 - 1
