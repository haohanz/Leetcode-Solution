class Solution(object):
    # Time: O(n)
    # Space: O(1)
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        def swap(arr, x, y):
            arr[x], arr[y] = arr[y], arr[x]
        
        def cmp(arr, x, y):
            return arr[x][0] ** 2 + arr[x][1] ** 2 - arr[y][0] ** 2 - arr[y][1] ** 2
        
        def quick_select(arr, l, r):
            pivot = random.randint(l, r)
            swap(arr, pivot, r)
            k = l
            for i in xrange(l, r):
                if cmp(arr, i, r) <= 0:
                    swap(arr, i, k)
                    k += 1
            swap(arr, k, r)
            return k
        
        l, r = 0, len(points) - 1
        while l < r:
            ptr = quick_select(points, l, r)
            if ptr == k: break
            if ptr > k:
                r = ptr - 1
            else:
                l = ptr + 1
            
        return points[:k]
