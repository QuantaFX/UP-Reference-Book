def mod_pow(b, e, m):
    res = 1 % m

    while e > 0:
        if e & 1:
            res = (res * b) % m
        b = (b * b) % m
        e >>= 1

    return res
