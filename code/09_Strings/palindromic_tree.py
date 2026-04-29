import sys

N = 200000
MAX = N * 2 + 5

par = [-1] * MAX
len_arr = [0] * MAX
node = [0] * MAX
cs = [0] * MAX
cnt = [0] * (N + 5)

child = [[-1] * 128 for _ in range(MAX)]
size = 0


def newNode(p=-1):
    global size
    cnt[size] = 0
    par[size] = p
    len_arr[size] = 0 if p == -1 else len_arr[p] + 2

    for i in range(128):
        child[size][i] = -1

    size += 1
    return size - 1


def get(i, c):
    if child[i][c] == -1:
        child[i][c] = newNode(i)
    return child[i][c]


def manachers(s):
    global size

    n = len(s)
    cn = n * 2 + 1

    for i in range(n):
        cs[i * 2] = -1
        cs[i * 2 + 1] = ord(s[i])
        
    size = 0

    odd = newNode()
    even = newNode()

    len_arr[odd] = -1

    cen = 0
    rad = 0

    for i in range(cn):
        node[i] = even if i % 2 == 0 else get(odd, cs[i])

    for i in range(1, cn):
        if i > rad:
            L = i - 1
            R = i + 1
        else:
            M = cen * 2 - i
            node[i] = node[M]

            if len_arr[node[M]] < rad - i:
                L = -1
                R = 0
            else:
                R = rad + 1
                L = i * 2 - R

                while len_arr[node[i]] > rad - i:
                    node[i] = par[node[i]]

        while L >= 0 and R < cn and cs[L] == cs[R]:
            if cs[L] != -1:
                node[i] = get(node[i], cs[L])
            L -= 1
            R += 1

        cnt[node[i]] += 1

        if i + len_arr[node[i]] > rad:
            rad = i + len_arr[node[i]]
            cen = i

    for i in range(size - 1, -1, -1):
        if par[i] != -1:
            cnt[par[i]] += cnt[i]


def countUniquePalindromes(s):
    manachers(s)
    return size


def countAllPalindromes(s):
    manachers(s)
    return sum(cnt[:size])


def longestPalindrome(s):
    manachers(s)

    n = len(s)
    cn = n * 2 + 1

    mx = 0
    for i in range(1, cn):
        if len_arr[node[mx]] < len_arr[node[i]]:
            mx = i

    pos = (mx - len_arr[node[mx]]) // 2
    return s[pos:pos + len_arr[node[mx]]]