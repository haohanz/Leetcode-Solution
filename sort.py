# merge sort
class Sort(object):
    def merge_sort(self, arr):
        def helper(start, end):
            if start >= end: return
            mid = (start + end) >> 1
            helper(start, mid)
            helper(mid + 1, end)
            i = start
            j = mid + 1
            k = 0
            ret = [0] * (end - start + 1)
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    ret[k] = arr[i]
                    k += 1
                    i += 1
                else:
                    ret[k] = arr[j]
                    k += 1
                    j += 1
            while i <= mid:
                ret[k] = arr[i]
                i += 1
                k += 1
            while j <= end:
                ret[k] = arr[j]
                j += 1
                k += 1
            for i in xrange(len(ret)):
                arr[i + start] = ret[i]
        helper(0, len(arr) - 1)
        print arr

    def quick_sort(self, arr):
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def partition(lo, hi):
            pivot = arr[hi]
            ptr = arr[lo]
            k = lo
            for i in xrange(lo, hi):
                if arr[i] < pivot:
                    swap(k, i)
                    k += 1
            swap(k, hi)
            return k

        def helper(lo, hi):
            if lo < hi:
                p = partition(lo, hi)
                helper(lo, p - 1)
                helper(p + 1, hi)

        helper(0, len(arr) - 1)
        print arr


s = Sort()
s.merge_sort([38,27,43,39])
s.merge_sort([38,27,43,39,39,39,40,0,1,39])
s.merge_sort([38,27,43,39,8,2,10])
s.merge_sort([38,27])
s.quick_sort([38,27,43,39])
s.quick_sort([38,27,43,39,39,39,40,0,1,39])
s.quick_sort([38,27,43,39,8,2,10])
s.quick_sort([38,27])
