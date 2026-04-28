def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_euclid(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


def modinv(a, m):
    g, x, y = extended_euclid(a, m)

    if g != 1:
        return 0  # no inverse

    return x % m