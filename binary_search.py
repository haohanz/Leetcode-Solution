# TODO Step 1: decide return range
# TODO Step 2: decide l, r according to return range
# TODO Step 3: decide close and open side according to l, r
# TODO Step 4: always move the close side first, with a mid+1 or mid-1 pos
# TODO Step 5: l < r
# TODO Step 6: return the close side

def findFirstGreaterEqual(arr, target): # left close right open
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)>>1
        if arr[mid] < target:
            l = mid + 1 # always raise left
        else:
            r = mid
    return l # return range [0 - len(arr)]

def findFirstGreater(arr, target): # left close right open
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)>>1
        if arr[mid] <= target:
            l = mid + 1 # always raise left
        else:
            r = mid
    return l # return range [0 - len(arr)]

def findLastSmallerEqual(arr, target): # left close right open
    l, r = -1, len(arr)-1
    while l < r:
        mid = (l+r+1)>>1
        if arr[mid] > target:
            r = mid - 1 # always raise left
        else:
            l = mid
    return r # return range [-1 - len(arr)-1]

def findLastSmaller(arr, target): # left close right open
    l, r = -1, len(arr)-1
    while l < r:
        mid = (l+r+1)>>1
        if arr[mid] >= target:
            r = mid - 1 # always raise left
        else:
            l = mid
    return r # return range [-1 - len(arr)-1]


arrs = [[], [1], [0,1,2,2,2,3], [0,1,2], [0,1,2]]
targets = [0, 1, 2, 3, -1]
for i in xrange(len(arrs)):
    print arrs[i], targets[i]

    print 'fisrt >=', findFirstGreaterEqual(arrs[i], targets[i])
    print 'fisrt >', findFirstGreater(arrs[i], targets[i])
    # print findLastEqual(arrs[i], targets[i])
    print 'last <=', findLastSmallerEqual(arrs[i], targets[i])
    print 'last <', findLastSmaller(arrs[i], targets[i])

