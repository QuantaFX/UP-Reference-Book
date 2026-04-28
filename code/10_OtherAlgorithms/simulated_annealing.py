import random
import math
import time


def simulated_annealing(n, seconds):
    rng = random.Random()

    sol = list(range(1, n + 1))
    rng.shuffle(sol)

    def score(arr):
        return sum(abs(arr[i] - arr[i - 1]) for i in range(1, n))

    cur = score(sol)

    T0 = 100.0
    T1 = 0.001
    start = time.time()
    iters = 0

    while True:
        if iters % 16 == 0:
            progress = (time.time() - start) / seconds
            if progress >= 1.0:
                break
            temp = T0 * (T1 / T0) ** progress

        a = rng.randint(0, n - 2)

        x, y = sol[a], sol[a + 1]

        delta = 0

        if a > 0:
            delta += abs(sol[a - 1] - y) - abs(sol[a - 1] - x)

        if a + 2 < n:
            delta += abs(x - sol[a + 2]) - abs(y - sol[a + 2])

        accept = delta <= 0 or rng.random() < math.exp(-delta / temp)

        if accept:
            sol[a], sol[a + 1] = sol[a + 1], sol[a]
            cur += delta

        iters += 1

    return cur, sol