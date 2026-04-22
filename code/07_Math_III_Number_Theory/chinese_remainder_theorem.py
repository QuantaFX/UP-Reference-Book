def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_min_x(num, rem):
    prod = 1
    for n in num:
        prod *= n

    result = 0
    for i in range(len(num)):
        prod_i = prod // num[i]
        _, inv_i, _ = gcd_extended(prod_i, num[i])
        result += rem[i] * prod_i * inv_i

    return result % prod

# Example Usage
num1 = [5, 7]
rem1 = [1, 3]
print("x is", find_min_x(num1, rem1)) 

num2 = [3, 4, 5]
rem2 = [2, 3, 1]
print("x is", find_min_x(num2, rem2))