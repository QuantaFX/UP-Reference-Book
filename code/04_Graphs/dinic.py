INF = float('inf')
class Dinic:
    def __init__(self, n, s, t):
        self.n, self.s, self.t = n, s, t
        self.edges = [] 
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, c, bi=False):
        self.adj[u].append(len(self.edges))
        self.edges.append([v, c, 0])
        self.adj[v].append(len(self.edges))
        self.edges.append([u, c if bi else 0, 0])

    def bfs(self):
        self.dist = [-1] * self.n
        self.dist[self.s] = 0
        q = deque([self.s])
        while q:
            u = q.popleft()
            for i in self.adj[u]:
                v, c, f = self.edges[i]
                if self.dist[v] < 0 and c > f:
                    self.dist[v] = self.dist[u] + 1
                    q.append(v)
        return self.dist[self.t] != -1
    
    def dfs(self, u, pushed):
        if pushed == 0 or u == self.t: return pushed
        while self.ptr[u] < len(self.adj[u]):
            i = self.adj[u][self.ptr[u]]
            v, c, f = self.edges[i]
            if self.dist[u]+1 == self.dist[v] and c > f:
                tr = self.dfs(v, min(pushed, c - f))
                if tr > 0:
                    self.edges[i][2] += tr
                    self.edges[i^1][2] -= tr
                    return tr
            self.ptr[u] += 1
        return 0

    def calc_max_flow(self):
        flow = 0
        while self.bfs():
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(self.s, INF)
                if not pushed:
                    break
                flow += pushed
        return flow