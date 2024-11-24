def solution(x, n):
    answer = []
    start = x
    for i in range(1, n + 1):
        num = x * i
        answer.append(num)
    return answer
