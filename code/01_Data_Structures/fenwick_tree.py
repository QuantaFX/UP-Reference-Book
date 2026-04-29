class Fenwick:
    def __init__(self, arr):
        self.n = len(arr)
        self.ar = [0] * self.n
        for i in range(self.n):
            self.ar[i] += arr[i]
            j = i | (i + 1)
            if j < self.n:
                self.ar[j] += self.ar[i]

    def sum(self, i):
        res = 0
        while i >= 0:
            res += self.ar[i]
            i = (i & (i + 1)) - 1
        return res

    def range_sum(self, i, j):
        return self.sum(j) - (self.sum(i - 1) if i > 0 else 0)

    def add(self, i, val):
        while i < self.n:
            self.ar[i] += val
            i |= i + 1

    def get(self, i):
        res = self.ar[i]
        if i > 0:
            lca = (i & (i + 1)) - 1
            i -= 1
            while i != lca:
                res -= self.ar[i]
                i = (i & (i + 1)) - 1
        return res

    def set(self, i, val):
        self.add(i, val - self.get(i))

    def range_add(self, l, r, val):
        self.add(l, val)
        if r + 1 < self.n:
            self.add(r + 1, -val)

    def point_query(self, i):
        return self.sum(i)