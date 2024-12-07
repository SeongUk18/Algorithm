def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fibo_dict = {}
    fibo_dict[0] = 0
    fibo_dict[1] = 1

    for i in range(2, n + 1):
        fibo_dict[i] = (fibo_dict[i - 1] + fibo_dict[i - 2])

    return fibo_dict[n] % 1234567
