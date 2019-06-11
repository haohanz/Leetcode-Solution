def build_arr(pattern):
    arr = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            arr[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = arr[j-1]
            else:
                i += 1
    print arr
    return arr

def kmp(text, pattern):
    arr = build_arr(pattern)
    i, j = 0, 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = arr[j-1]
            else:
                i += 1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1

a = "aabaaabaaac"
b = "aabaaac"
print kmp(a, b)
