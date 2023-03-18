T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    first_num = 0
    last_num = 0
    if N % H == 0:
        first_num = H
        last_num = N//H
    else:
        first_num = N % H
        last_num = N // H + 1
    print("%d0%d" % (first_num, last_num))
