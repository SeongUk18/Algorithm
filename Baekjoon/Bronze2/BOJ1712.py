A, B, C = map(int, input().split())


def solve(fixed_cost, variable_cost, price):
    #  가격이 원가보다 낮거나 같을때, 가격이 0일 때
    if price <= variable_cost or price == 0:
        return -1
    # 손익 분기점 계산(고정비/가격-원가)-> 몫+1
    else:
        return fixed_cost // (price - variable_cost) + 1


print(solve(A, B, C))
