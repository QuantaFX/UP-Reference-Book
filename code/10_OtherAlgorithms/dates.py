def c_div(a, b):
    return int(a / b)

def date_to_int(y, m, d):
    k = c_div(m - 14, 12)

    return (
        1461 * (y + 4800 + k) // 4
        + 367 * (m - 2 - k * 12) // 12
        - 3 * ((y + 4900 + k) // 100) // 4
        + d - 32075
    )


def int_to_day(jd):
    return jd % 7


def int_to_date(jd):
    x = jd + 68569
    n = 4 * x // 146097
    x -= (146097 * n + 3) // 4

    i = (4000 * (x + 1)) // 1461001
    x -= 1461 * i // 4 - 31

    j = 80 * x // 2447
    d = x - 2447 * j // 80

    x = j // 11
    m = j + 2 - 12 * x
    y = 100 * (n - 49) + i + x

    return y, m, d