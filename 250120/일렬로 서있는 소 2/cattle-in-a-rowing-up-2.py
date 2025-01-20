N = int(input())
A = list(map(int, input().split()))

answer = 0

for i in range(N - 2):
    first = A[i]
    for j in range(i + 1, N - 1):
        if first <= A[j]:
            second = A[j]
            for k in range(j + 1, N):
                if second <= A[k]:
                    answer += 1
                    # print(first, second, A[k])

print(answer)