# 길이 입력
N = int(input())
# 합을 구할 문자열 입력
num_string = input()

# 문자열 합 계산
num_sum = 0
for i in num_string:
    num_sum += int(i)

print(num_sum)