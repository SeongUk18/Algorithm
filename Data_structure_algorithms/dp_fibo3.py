# 하향식 DP 피보나치 (재귀, Memoization)
def fib_top_down(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    return fib_top_down(n - 1) + fib_top_down(n - 2)


print(fib_top_down(10))  # Output: 55
