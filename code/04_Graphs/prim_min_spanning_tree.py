import heapq

def prim(n, adj, start=0):
    visited = [False] * n
    pq = [(0, start, -1)]

    total_weight = 0
    mst = []

    while pq:
        w, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, w))
            total_weight += w

        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))

    return mst, total_weight