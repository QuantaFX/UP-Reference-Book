_fact_cache = []
_last_p = -1

def lucas(n, k, p):
    if k < 0 or k > n:
        return 0
    if k == 0 or n == k:
        return 1

    global _fact_cache, _last_p
    if _last_p != p:
        _fact_cache = [1] * p
        for i in range(2, p):
            _fact_cache[i] = (_fact_cache[i - 1] * i) % p
        _last_p = p

    res_num = 1
    res_den = 1

    while n > 0 or k > 0:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        res_num = (res_num * _fact_cache[ni]) % p
        res_den = (res_den * _fact_cache[ki] * _fact_cache[ni - ki]) % p
        n //= p
        k //= p
    return (res_num * pow(res_den, p - 2, p)) % p
# Input Format: print(lucas(n, k, p))