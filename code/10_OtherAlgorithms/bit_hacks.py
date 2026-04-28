def snoob(x):
    y = x & -x
    z = x + y
    return z | (((x ^ z) // y) >> 2)