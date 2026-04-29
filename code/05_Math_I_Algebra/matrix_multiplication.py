MOD = 998244353

def multiply(A, B):
    p = len(A)
    q = len(A[0])
    r = len(B[0])

    if len(B) != q:
        raise ValueError("Dimension mismatch")

    AB = [[0] * r for _ in range(p)]

    for i in range(p):
        for j in range(q):
            for k in range(r):
                AB[i][k] = (AB[i][k] + A[i][j] * B[j][k]) % MOD

    return AB