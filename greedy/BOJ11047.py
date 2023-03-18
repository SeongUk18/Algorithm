n, k = map(int, input().split())
# 지폐들 저장 배열
coins = []
# 지폐 저장
for _ in range(n):
    coins.append(int(input()))
# 오름차순 정렬
coins.sort(reverse=True)

numbers = 0
for i in coins:
    # 돈이 0일때 까지 반복
    if k == 0:
        break
    else:
        # 잔돈 갯수 추가 (몫)
        numbers += k // i
        # 잔돈 갯수 추가에 따른 값 변경 (나머지)
        k = k % i
print(numbers)