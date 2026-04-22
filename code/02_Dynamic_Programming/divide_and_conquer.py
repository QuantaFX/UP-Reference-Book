INF = float('inf')

def solve_dp(g, k_L, k_R, n_L, n_R, dp, cost_func):
    if n_L > n_R:
        return

    n_M = (n_L + n_R) // 2
    best_k = -1
    dp[g][n_M] = INF

    for k in range(k_L, min(n_M, k_R) + 1):
        current_val = dp[g - 1][k] + cost_func(k + 1, n_M)
        if current_val < dp[g][n_M]:
            dp[g][n_M] = current_val
            best_k = k

    solve_dp(g, k_L, best_k, n_L, n_M - 1, dp, cost_func)
    solve_dp(g, best_k, k_R, n_M + 1, n_R, dp, cost_func)