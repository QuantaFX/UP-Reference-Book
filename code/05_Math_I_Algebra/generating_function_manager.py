MOD = 998244353

def mod_pow(base, exp):
    res = 1
    base %= MOD
    while exp:
        if exp & 1:
            res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
    return res


class GF_Manager:
    DEPTH = 23

    def __init__(self):
        self.prim = [0] * (self.DEPTH + 1)
        self.prim_inv = [0] * (self.DEPTH + 1)
        self.two_inv = [0] * (self.DEPTH + 1)
        self.set_up_primitives()

    def set_up_primitives(self):
        self.prim[self.DEPTH] = 31
        self.prim_inv[self.DEPTH] = mod_pow(self.prim[self.DEPTH], MOD - 2)
        self.two_inv[self.DEPTH] = mod_pow(1 << self.DEPTH, MOD - 2)

        for n in range(self.DEPTH - 1, -1, -1):
            self.prim[n] = self.prim[n + 1] * self.prim[n + 1] % MOD
            self.prim_inv[n] = mod_pow(self.prim[n], MOD - 2)
            self.two_inv[n] = mod_pow(1 << n, MOD - 2)

    def NTT(self, A, n, is_inverse=False):
        if n == 0:
            return A[:]

        half = 1 << (n - 1)
        even = A[0::2]
        odd = A[1::2]

        even = self.NTT(even, n - 1, is_inverse)
        odd = self.NTT(odd, n - 1, is_inverse)

        res = [0] * (1 << n)
        w1 = self.prim_inv[n] if is_inverse else self.prim[n]
        w = 1

        for i in range(half):
            t = w * odd[i] % MOD
            res[i] = (even[i] + t) % MOD
            res[i + half] = (even[i] - t) % MOD
            w = w * w1 % MOD

        return res

    def mult(self, A, B):
        an, bn = len(A), len(B)
        degree = an + bn - 1

        n = 0
        while (1 << n) < degree:
            n += 1

        size = 1 << n
        tA = A + [0] * (size - an)
        tB = B + [0] * (size - bn)

        tA = self.NTT(tA, n)
        tB = self.NTT(tB, n)

        for i in range(size):
            tA[i] = tA[i] * tB[i] % MOD

        tA = self.NTT(tA, n, True)

        inv = self.two_inv[n]
        return [(x * inv) % MOD for x in tA[:degree]]

    def horners(self, F, x):
        ans = 0
        for coef in reversed(F):
            ans = (ans * x + coef) % MOD
        return ans