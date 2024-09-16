# 상향식 DP 피보나치 (반복문, Tabulation)
def fib_bottom_up(n):
    if n <= 1:
        return n

    dp = [0 for _ in range(n + 1)]

    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fib_bottom_up(10))  # Output: 55
