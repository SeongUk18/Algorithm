def solution(s):
    N = len(s)
    middle = N // 2
    if N % 2 == 1:
        answer = s[middle]
    else:
        answer = s[middle - 1: middle + 1]
    return answer
