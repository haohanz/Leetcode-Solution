# Select top k values from array
class QuickSelect(object):
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(self, arr, start, end):
        if start > end: return
        pivot = arr[end]
        ptr = start
        for i in xrange(start, end):
            if arr[i] < pivot:
                self.swap(arr, ptr, i)
                ptr += 1
        self.swap(arr, ptr, end)
        return ptr

    def run(self, arr, k):
        start, end = 0, len(arr) - 1
        while True:
            pivot = self.partition(arr, start, end)
            if pivot == k:
                print arr[:k]
                return arr[:k]
            elif pivot > k:
                end = pivot - 1
            else:
                start = pivot + 1

s = QuickSelect()
s.run([3,1,5,1,3,4,1,5], 4)
