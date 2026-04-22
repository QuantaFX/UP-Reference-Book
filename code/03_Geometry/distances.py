
# Distance: Point to 2D Line (ax + by + c = 0)
def dist_pt_line_eq(p, a, b, c):
    return abs(a*p.real + b*p.imag + c) / math.hypot(a, b)

# Distance: Point to 2D Line through points a and b
def dist_pt_line(p, a, b):
    cp = (p - a).conjugate() * (b - a)
    return abs(cp.imag) / abs(b - a)

# Distance: Point to 3D Plane (ax + by + cz + d = 0)
def dist_pt_plane(p, a, b, c, d):
    # math.hypot supports 3+ arguments in Python 3.8+
    return abs(a*p.x + b*p.y + c*p.z + d) / math.hypot(a,b,c)

# Distance: Shortest distance between 3D lines AB and CD
def dist_line_3d(A, B, C, D):
    u, v, w = B - A, D - C, A - C
    a, b = u.dot(u), u.dot(v)
    c, d, e = v.dot(v), u.dot(w), v.dot(w)
    det = a * c - b * b
    if det < 1e-9: # Parallel lines
        s, t = 0.0, d / b if b > c else e / c
    else: # Skew lines
        s = (b * e - c * d) / det
        t = (a * e - b * d) / det
    p1 = P3(A.x + u.x*s, A.y + u.y*s, A.z + u.z*s)
    p2 = P3(C.x + v.x*t, C.y + v.y*t, C.z + v.z*t)
    vec = p1 - p2
    return math.sqrt(vec.dot(vec))