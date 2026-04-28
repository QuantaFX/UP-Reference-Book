from collections import deque

def stable_marriage(n, m_pref, w_pref):
    w_rank = [[0] * n for _ in range(n)]

    for w in range(n):
        for i, man in enumerate(w_pref[w]):
            w_rank[w][man] = i

    q = deque(range(n))

    at = [0] * n

    eng = [-1] * n

    res = [-1] * n

    while q:
        m = q.popleft()

        while at[m] < n:
            w = m_pref[m][at[m]]
            at[m] += 1

            if eng[w] == -1:
                eng[w] = m
                res[m] = w
                break

            if w_rank[w][m] < w_rank[w][eng[w]]:
                q.append(eng[w])
                eng[w] = m
                res[m] = w
                break

    return res
