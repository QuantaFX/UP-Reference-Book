import math

class BinaryLifting:
    def __init__(self, adj):
        self.n = len(adj)
        self.LOG = math.ceil(math.log2(self.n)) + 1
        self.adj = adj

        self.dep = [0] * self.n
        self.par = [[-1] * self.LOG for _ in range(self.n)]

        self.build(0)

    def dfs(self, u, p):
        self.par[u][0] = p
        for v in self.adj[u]:
            if v != p:
                self.dep[v] = self.dep[u] + 1
                self.dfs(v, u)

    def build(self, root):
        self.dfs(root, root)

        for k in range(1, self.LOG):
            for u in range(self.n):
                self.par[u][k] = self.par[self.par[u][k-1]][k-1]

    def lift(self, u, k):
        for i in range(self.LOG):
            if k & (1 << i):
                u = self.par[u][i]
        return u

    def lca(self, u, v):
        if self.dep[u] < self.dep[v]:
            u, v = v, u

        u = self.lift(u, self.dep[u] - self.dep[v])

        if u == v:
            return u

        for k in reversed(range(self.LOG)):
            if self.par[u][k] != self.par[v][k]:
                u = self.par[u][k]
                v = self.par[v][k]

        return self.par[u][0]