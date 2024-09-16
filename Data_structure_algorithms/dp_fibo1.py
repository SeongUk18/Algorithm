# 기본 재귀 방식 피보나치
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


print(fib_recursive(10))  # Output: 55
