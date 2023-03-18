# 사람 수
people = int(input())

times = input().split()

# print(times)
# 정수 형으로 변환 및 정렬
for i in range(len(times)):
    times[i] = int(times[i])
times.sort()

before_time = 0
result = 0
# 기다리는 시간 + total 시간 계산
for i in range(len(times)):
    before_time = before_time + times[i]
    result = result + before_time

print(result)