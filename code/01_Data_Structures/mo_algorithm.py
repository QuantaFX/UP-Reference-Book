from collections import defaultdict

LOGN = 21

def hilbert_order(x, y, pow, rotate):
    if pow == 0:
        return 0
    hpow = 1 << (pow - 1)
    if x < hpow:
        if y < hpow:
            seg = 0
        else:
            seg = 3
    else:
        if y < hpow:
            seg = 1
        else:
            seg = 2
    seg = (seg + rotate) & 3
    rotate_delta = [3, 0, 0, 1]
    nx = x & (x ^ hpow)
    ny = y & (y ^ hpow)
    nrot = (rotate + rotate_delta[seg]) & 3
    sub_sq_size = 1 << (2 * pow - 2)
    ans = seg * sub_sq_size
    add = hilbert_order(nx, ny, pow - 1, nrot)
    if seg == 1 or seg == 2:
        ans += add
    else:
        ans += sub_sq_size - add - 1
    return ans

class Query:
    def __init__(self, idx, l, r):
        self.id = idx
        self.l = l
        self.r = r
        self.ord = hilbert_order(l, r, LOGN, 0)

    def __lt__(self, other):
        return self.ord < other.ord

def mo_algorithm(arr, queries):
    queries.sort()

    freq = defaultdict(int)
    distinct = 0

    def add(i):
        nonlocal distinct
        x = arr[i]
        freq[x] += 1
        if freq[x] == 1:
            distinct += 1

    def remove(i):
        nonlocal distinct
        x = arr[i]
        freq[x] -= 1
        if freq[x] == 0:
            distinct -= 1
    ans = [0] * len(queries)
    l = 0
    r = -1
    for q in queries:
        while r < q.r:
            r += 1
            add(r)
        while r > q.r:
            remove(r)
            r -= 1
        while l > q.l:
            l -= 1
            add(l)
        while l < q.l:
            remove(l)
            l += 1
        ans[q.id] = distinct
    return ans
