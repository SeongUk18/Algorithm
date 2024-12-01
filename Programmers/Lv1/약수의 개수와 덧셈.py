def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if num == 1:
            num_list = [1]
        else:
            num_list = [1, num]
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                num_list.append(i)
                # print(i)
        if len(num_list) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer
