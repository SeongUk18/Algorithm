A = input()
N = len(A)

answer = 0
for i in range(N - 1):
    for j in range(i, N):
        if A[i] == "(":
            if A[j] == ")":
                answer += 1

print(answer)