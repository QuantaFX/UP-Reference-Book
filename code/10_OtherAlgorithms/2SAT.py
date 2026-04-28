class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.N = 2 * n
        self.adj = [[] for _ in range(self.N)]

    def var(self, x):
        return x << 1

    def neg(self, x):
        return x ^ 1

    def add_imp(self, x, y):
        self.adj[x].append(y)

    def add_or(self, x, y):
        self.add_imp(self.neg(x), y)
        self.add_imp(self.neg(y), x)

    def sat(self):
        n = self.N
        adj = self.adj

        index = 0
        stack = []
        onstack = [False] * n
        ids = [-1] * n
        low = [0] * n
        comp = [-1] * n
        self.time = 0
        self.comp_id = 0

        def dfs(u):
            nonlocal index

            ids[u] = low[u] = index
            index += 1
            stack.append(u)
            onstack[u] = True

            for v in adj[u]:
                if ids[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif onstack[v]:
                    low[u] = min(low[u], ids[v])

            if low[u] == ids[u]:
                while True:
                    v = stack.pop()
                    onstack[v] = False
                    comp[v] = self.comp_id
                    if v == u:
                        break
                self.comp_id += 1

        for i in range(n):
            if ids[i] == -1:
                dfs(i)

        for i in range(0, n, 2):
            if comp[i] == comp[i ^ 1]:
                return False

        return True