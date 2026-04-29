MOD = 998244353
PRIMITIVE_ROOT = 3

def mod_pow(base, exp, mod=MOD):
    res = 1
    base %= mod
    while exp:
        if exp & 1:
            res = res * base % mod
        base = base * base % mod
        exp >>= 1
    return res

class Num:
    def __init__(self, x=0):
        self.x = x % MOD

    def __add__(self, other):
        return Num(self.x + other.x)

    def __sub__(self, other):
        return Num(self.x - other.x)

    def __mul__(self, other):
        return Num(self.x * other.x)

    def __truediv__(self, other):
        return self * other.inv()

    def inv(self):
        return Num(mod_pow(self.x, MOD - 2))

    def pow(self, p):
        return Num(mod_pow(self.x, p))

    def __repr__(self):
        return str(self.x)

def ntt(a, invert=False):
    n = len(a)

    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = mod_pow(PRIMITIVE_ROOT, (MOD - 1) // length)
        if invert:
            wlen = mod_pow(wlen, MOD - 2)

        for i in range(0, n, length):
            w = 1
            half = length // 2
            for j in range(i, i + half):
                u = a[j]
                v = Num(a[j + half].x * w % MOD)
                a[j] = u + v
                a[j + half] = u - v
                w = w * wlen % MOD

        length <<= 1

    if invert:
        inv_n = mod_pow(n, MOD - 2)
        for i in range(n):
            a[i] = Num(a[i].x * inv_n % MOD)

def multiply(A, B):
    n = 1
    while n < len(A) + len(B):
        n <<= 1

    fa = [Num(x) for x in A] + [Num(0)] * (n - len(A))
    fb = [Num(x) for x in B] + [Num(0)] * (n - len(B))

    ntt(fa)
    ntt(fb)

    for i in range(n):
        fa[i] = fa[i] * fb[i]

    ntt(fa, True)

    return [fa[i].x for i in range(len(A) + len(B) - 1)]

def poly_inv(x, l):
    if l == 1:
        return [mod_pow(x[0], MOD - 2)]

    y = poly_inv(x, (l + 1) // 2)

    n = 1
    while n < 2 * l:
        n <<= 1

    A = x[:l] + [0] * (n - l)
    B = y[:] + [0] * (n - len(y))

    A = [Num(v) for v in A]
    B = [Num(v) for v in B]

    ntt(A)
    ntt(B)

    for i in range(n):
        B[i] = B[i] * (Num(2) - A[i] * B[i])

    ntt(B, True)

    return [B[i].x % MOD for i in range(l)]

def poly_sqrt(x, l):
    if l == 1:
        assert x[0] == 1
        return [1]

    y = poly_sqrt(x, l // 2)
    inv_y = poly_inv(y, l // 2)

    n = 1
    while n < 2 * l:
        n <<= 1

    T1 = x[:l] + [0] * (n - l)
    T2 = inv_y[:] + [0] * (n - len(inv_y))

    T1 = [Num(v) for v in T1]
    T2 = [Num(v) for v in T2]

    ntt(T1)
    ntt(T2)

    for i in range(n):
        T2[i] = T1[i] * T2[i]

    ntt(T2, True)

    inv2 = (MOD + 1) // 2
    res = []
    for i in range(l):
        val = (y[i] + T2[i].x) * inv2 % MOD
        res.append(val)

    return res
