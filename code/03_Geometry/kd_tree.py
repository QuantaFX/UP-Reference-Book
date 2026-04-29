import heapq

EPS = 1e-9
def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
class KDTree:
    def __init__(self, points):
        self.p = points[:]
        self.n = len(points)
        self.build(0, self.n, 0)
    def build(self, L, R, dvx):
        if R - L <= 1:
            return
        mid = (L + R) // 2
        if dvx:
            self.p[L:R] = sorted(self.p[L:R], key=lambda x: x[0])
        else:
            self.p[L:R] = sorted(self.p[L:R], key=lambda x: x[1])
        self.build(L, mid, not dvx)
        self.build(mid + 1, R, not dvx)
    def knn(self, x, y, k=1, r=-1):
        self.qx = x
        self.qy = y
        self.k = k
        self.prune = float("inf") if r < 0 else r * r
        self.heap = []
        self._dfs(0, self.n, False)
        res = [p for _, p in sorted(self.heap, reverse=True)]
        return res
    def _dfs(self, L, R, dvx):
        if R - L <= 0:
            return
        mid = (L + R) // 2
        p = self.p[mid]
        dx = self.qx - p[0]
        dy = self.qy - p[1]
        D = dx * dx + dy * dy
        if D <= self.prune:
            heapq.heappush(self.heap, (-D, p))
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        delta = dx if dvx else dy
        nL, nR = L, mid
        fL, fR = mid + 1, R
        if delta > 0:
            nL, fL = fL, nL
            nR, fR = fR, nR
        self._dfs(nL, nR, not dvx)
        if len(self.heap) < self.k or delta * delta <= self.prune:
            self._dfs(fL, fR, not dvx)