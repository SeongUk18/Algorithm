def knapsack(weights, values, W):
    n = len(weights)  # 아이템의 수
    # DP 테이블 초기화
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):  # i 번째 아이템까지 고려
        for w in range(1, W + 1):  # 배낭 용량 w 까지 고려
            if weights[i - 1] <= w:  # 현재 아이템이 배낭에 들어갈 수 있는 경우
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:  # 들어갈 수 없는 경우
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]  # 최종적 최대 가치


# 테스트 케이스
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack(weights, values, W))  # Output: 7
