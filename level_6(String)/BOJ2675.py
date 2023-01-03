N = int(input())

for i in range(N):
    # 반복 수, 문자열 하나씩 입력
    R, S = input().split()
    result = ""
    # 빈 문자열에 입력 받은 문자열 반복 횟수 만큼 추가
    for k in S:
        result += k*int(R)
    print(result)