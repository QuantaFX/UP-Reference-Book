import math

class SparseTable2D:
    def __init__(self, A):
        self.A = A
        self.n = len(A)
        self.m = len(A[0])

        self.LOGN = int(math.log2(self.n)) + 1
        self.LOGM = int(math.log2(self.m)) + 1

        self.lg = [0] * (max(self.n, self.m) + 1)
        for i in range(2, len(self.lg)):
            self.lg[i] = self.lg[i // 2] + 1

        self.st = [[[[0] * self.m for _ in range(self.n)]
                    for _ in range(self.LOGM)]
                   for _ in range(self.LOGN)]

        self.build()

    def build(self):
        for i in range(self.n):
            for j in range(self.m):
                self.st[0][0][i][j] = self.A[i][j]

        for bj in range(1, self.LOGM):
            for i in range(self.n):
                for j in range(self.m - (1 << bj) + 1):
                    self.st[0][bj][i][j] = max(
                        self.st[0][bj - 1][i][j],
                        self.st[0][bj - 1][i][j + (1 << (bj - 1))]
                    )

        for bi in range(1, self.LOGN):
            for i in range(self.n - (1 << bi) + 1):
                for j in range(self.m):
                    self.st[bi][0][i][j] = max(
                        self.st[bi - 1][0][i][j],
                        self.st[bi - 1][0][i + (1 << (bi - 1))][j]
                    )

        for bi in range(1, self.LOGN):
            for bj in range(1, self.LOGM):
                for i in range(self.n - (1 << bi) + 1):
                    for j in range(self.m - (1 << bj) + 1):
                        self.st[bi][bj][i][j] = max(
                            self.st[bi - 1][bj - 1][i][j],
                            self.st[bi - 1][bj - 1][i + (1 << (bi - 1))][j],
                            self.st[bi - 1][bj - 1][i][j + (1 << (bj - 1))],
                            self.st[bi - 1][bj - 1][i + (1 << (bi - 1))][j + (1 << (bj - 1))]
                        )

    def query(self, x1, y1, x2, y2):
        kx = self.lg[x2 - x1 + 1]
        ky = self.lg[y2 - y1 + 1]

        return max(
            self.st[kx][ky][x1][y1],
            self.st[kx][ky][x2 - (1 << kx) + 1][y1],
            self.st[kx][ky][x1][y2 - (1 << ky) + 1],
            self.st[kx][ky][x2 - (1 << kx) + 1][y2 - (1 << ky) + 1]
        )
# Input Format: st = SparseTable2D(grid)
#               print(st.query(1, 1, 2, 2))