num1, num2 = input().split()
# 슬라이싱을 이용한 문자열 뒤집기
num1 = num1[::-1]
num2 = num2[::-1]
# 큰 숫자 찾기
answer = max(num1, num2)

print(answer)