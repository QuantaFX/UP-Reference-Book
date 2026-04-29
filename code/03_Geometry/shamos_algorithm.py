import math

EPS = 1e-9
def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]
def dist_pt_line(p, a, b):
    ab = sub(b, a)
    ap = sub(p, a)
    return abs(cross(ab, ap)) / (math.hypot(ab[0], ab[1]) + EPS)
def convex_hull(points):
    points = sorted(points)
    def build():
        hull = []
        for p in points:
            while len(hull) >= 2 and cross(sub(hull[-1], hull[-2]), sub(p, hull[-1])) <= EPS:
                hull.pop()
            hull.append(p)
        return hull
    lower = build()
    upper = build()
    return lower[:-1] + upper[:-1]
def shamos(p):
    h = convex_hull(p)
    k = len(h)

    if k <= 2:
        return 0.0

    d = float("inf")
    j = 1

    for i in range(k):
        ni = (i + 1) % k

        a = h[i]
        b = h[ni]

        while True:
            nj = (j + 1) % k
            if dist_pt_line(h[nj], a, b) > dist_pt_line(h[j], a, b):
                j = nj
            else:
                break
        d = min(d, dist_pt_line(h[j], a, b))
    return d