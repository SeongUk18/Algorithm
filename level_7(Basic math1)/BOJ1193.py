number = int(input())
# 몇번째 라인인지와 라인 최댓값 구하기
i = 1
sum_i = 1
while True:
    if number <= sum_i:
        break
    i += 1
    sum_i += i


def solve(line, sum_number, input_number):
    # 라인이 짝수 일때 분자 증가 분모 감소
    if line % 2 == 0:
        numerator = 1
        denominator = line
        for _ in range(line+input_number-sum_number-1):
            numerator += 1
            denominator -= 1
    # 라인이 홀수 일때, 분자 감소 분모 증가
    elif line % 2 == 1:
        numerator = line
        denominator = 1
        for _ in range(line+input_number-sum_number-1):
            numerator -= 1
            denominator += 1
    print(str(numerator)+"/"+str(denominator))


solve(i, sum_i, number)