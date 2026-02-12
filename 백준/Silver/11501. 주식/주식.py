t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    max_price = 0

    for i in range(n - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]

    print(profit)