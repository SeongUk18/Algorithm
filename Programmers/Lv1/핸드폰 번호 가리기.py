def solution(phone_number):
    answer = ''
    n = len(phone_number)

    for i in range(n):
        if n - i < 5:
            answer += str(phone_number[i])
        else:
            answer += "*"
    return answer
