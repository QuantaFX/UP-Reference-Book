import math

EPS = 1e-9

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def in_polygon(q, p):
    n = len(p)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = p[i]
        xj, yj = p[j]
        xq, yq = q

        intersect = ((yi > yq) != (yj > yq)) and (
            xq < (xj - xi) * (yq - yi) / (yj - yi + EPS) + xi
        )

        if intersect:
            inside = not inside

        j = i

    return inside

def on_polygon(q, p):
    n = len(p)

    for i in range(n):
        j = (i + 1) % n

        a = p[i]
        b = p[j]

        if abs(dist(a, q) + dist(q, b) - dist(a, b)) < EPS:
            return True

    return False