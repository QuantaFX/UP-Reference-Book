EPS = 1e-9
def projLine(p, a, b): # Project point p onto line segment ab
    v = b - a
    scalar = ((p - a) * v.conjugate()).real / abs(v)**2
    return a + v * scalar

def rotate(c, p, t): # Rotate point p around center c by t radians
    return c + (p - c) * cmath.rect(1, t)

def CL_inter(c, r, a, b):
    p = projLine(c, a, b)
    d = abs(c - p)
    ans = []
    
    if d > r + EPS: pass # None
    elif d > r - EPS: ans.append(p) # Tangent
    elif d < EPS: # Diameter
        v = r * (b - a) / abs(b - a)
        ans.append(c + v)
        ans.append(c - v)
    else: # Secant
        t = math.acos(d / r)
        p = c + (p - c) * r / d
        ans.append(rotate(c, p, t))
        ans.append(rotate(c, p, -t))
    return ans