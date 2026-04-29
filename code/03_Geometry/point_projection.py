EPS = 1e-9

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def scale(v, k):
    return [k * x for x in v]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def norm(v):
    return dot(v, v)

def proj(p, v):
    v_norm = norm(v)
    if v_norm < EPS:
        return [0] * len(p)
    return scale(v, dot(p, v) / v_norm)

def proj_line(p, a, b):
    ab = sub(b, a)
    ab_norm = norm(ab)
    if ab_norm < EPS:
        return a[:]

    t = dot(sub(p, a), ab) / ab_norm
    return add(a, scale(ab, t))

def proj_seg(p, a, b):
    ab = sub(b, a)
    ab_norm = norm(ab)
    if ab_norm < EPS:
        return a[:]

    t = dot(sub(p, a), ab) / ab_norm
    t = max(0.0, min(1.0, t))

    return add(a, scale(ab, t))

def proj_plane(p, a, b, c, d):
    n = [a, b, c]
    n_norm = norm(n)
    if n_norm < EPS:
        return p[:]

    dist = (dot(p, n) + d) / n_norm
    return sub(p, scale(n, dist))