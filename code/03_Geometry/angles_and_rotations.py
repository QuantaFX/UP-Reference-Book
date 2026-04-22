def angle(a, b, c): # angle formed by abc in radians: PI < x <= PI
    return abs((arg(a-b) - arg(c-b)) % (2 * math.pi))
def rotate(p, a, d): # rotate point a about pivot p CCW at d radians
    return p + (a - p) * complex(math.cos(d), math.sin(d))