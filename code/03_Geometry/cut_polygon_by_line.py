EPS = 1e-9

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def line_inter(p1, p2, a, b):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = a
    x4, y4 = b

    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < EPS:
        return p1

    px = (
        (x1 * y2 - y1 * x2) * (x3 - x4)
        - (x1 - x2) * (x3 * y4 - y3 * x4)
    ) / den

    py = (
        (x1 * y2 - y1 * x2) * (y3 - y4)
        - (y1 - y2) * (x3 * y4 - y3 * x4)
    ) / den

    return (px, py)

def cut(poly, a, b):
    n = len(poly)
    res = []

    for i in range(n):
        j = (i - 1 + n) % n

        c1 = cross(a, b, poly[j])
        c2 = cross(a, b, poly[i])

        if c1 >= -EPS:
            res.append(poly[j])

        if c1 * c2 < -EPS:
            inter = line_inter(poly[j], poly[i], a, b)
            res.append(inter)

    return res