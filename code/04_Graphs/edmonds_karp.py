INF = float('inf')
class EdmondsKarp:
    def __init__(self, n, s, t):
        self.n, self.s, self.t = n, s, t
        self.adj = [[] for _ in range(n)]
        self.res = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, w):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.res[u][v] += w

    def bfs(self):
        self.par = [-1] * self.n
        self.par[self.s] = self.s
        q = deque([self.s])
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if self.res[u][v] > 0 and self.par[v] == -1:
                    self.par[v] = u
                    if v == self.t:
                        return True
                    q.append(v)
        return False

    def calc_max_flow(self):
        ans = 0
        while self.bfs():
            flow = INF
            u = self.t
            while u != self.s:
                p = self.par[u]
                flow = min(flow, self.res[p][u])
                u = p
            u = self.t
            while u != self.s:
                p = self.par[u]
                self.res[p][u] -= flow
                self.res[u][p] += flow
                u = p
            ans += flow
        return ans