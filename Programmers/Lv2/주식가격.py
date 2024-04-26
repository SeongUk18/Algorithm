def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [0]
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            price = stack.pop()
            answer[price] = i - price
        stack.append(i)

    while stack:
        price = stack.pop()
        answer[price] = len(prices) - 1 - price

    return answer