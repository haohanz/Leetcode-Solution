from collections import defaultdict
class PairSum(object):
    def run(self, max_val, forward, backward):
        D_forward = defaultdict(list)
        D_backward = defaultdict(list)
        for idx, dist in forward:
            D_forward[dist].append(idx)
        for idx, dist in backward:
            D_backward[dist].append(idx)
        forward = sorted(D_forward.keys())
        backward = sorted(D_backward.keys())
        i, j = 0, len(backward) - 1
        max_res = 0
        D = defaultdict(list)
        while i < len(forward) and j >= 0:
            val = forward[i] + backward[j]
            if val > max_val:
                j -= 1
            elif val >= max_res:
                max_res = max(max_res, val)
                for x in D_forward[forward[i]]:
                    for y in D_backward[backward[j]]:
                        D[val].append([x, y])
                i += 1
            else:
                i += 1
        print D[max_res]
        return D[max_res]

s = PairSum()
s.run(10000, [[1, 2000],[2,2000],[3, 5000],[4,2000]], [[1, 5000],[2, 2000],[3, 8000],[4, 8000]])
