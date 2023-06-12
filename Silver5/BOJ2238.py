# 경매 결과 딕셔너리로 저장
price_dic = dict()
# 상한가, 경매 참여 갯수
U, N = map(int, input().split())

for _ in range(N):
    person, price = input().split()
    # 상한가 이상 값 받지 않기
    if int(price) <= U:
        price_dic[price] = price_dic.get(price, list()) + [person]
# 가장 적은 수 찾기
min_count = min([len(i) for i in price_dic.values()])
#
min_key = min([int(i) for i in price_dic.keys() if len(price_dic[i]) == min_count])

print(price_dic[str(min_key)][0], min_key)