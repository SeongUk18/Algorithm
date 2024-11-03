amount = int(input())

chart = list(map(int, input().split()))


def bnp(chart, amount):
    cur_amount = amount
    cur_stock = 0

    for price in chart:
        if price <= cur_amount:
            cur_stock += cur_amount // price
            cur_amount = cur_amount % price

    # print(cur_stock)
    return chart[-1] * cur_stock + cur_amount


def timing(chart, amount):
    cur_price = chart[0]
    cur_amount = amount
    cur_stock = 0
    buy_count = 0
    sell_count = 0

    for price in chart[1:]:
        if price < cur_price:
            buy_count += 1
            sell_count = 0

            if buy_count >= 3:
                cur_stock += cur_amount // price
                cur_amount = cur_amount % price
                buy_count = 0

        elif price > cur_price:
            sell_count += 1
            buy_count = 0

            if sell_count == 3:
                cur_amount += price * cur_stock
                cur_stock = 0
                sell_count = 0

    return chart[-1] * cur_stock + cur_amount


bnp_amount = bnp(chart, amount)
timing_amount = timing(chart, amount)

if bnp_amount < timing_amount:
    print("TIMING")
elif bnp_amount > timing_amount:
    print("BNP")
else:
    print("SAMESAME")
