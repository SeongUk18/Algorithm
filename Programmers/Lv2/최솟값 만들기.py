def solution(A, B):
    N = len(A)
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(N):
        answer += A[i] * B[i]

    return answer
