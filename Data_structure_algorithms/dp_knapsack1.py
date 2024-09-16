# 기본 재귀 방식 0-1 배낭 문제
def knapsack_recursive(weights, values, W, n):
    # 기저 사례
    if n == 0 or W == 0:
        return 0
    # 물건을 못 넣을때
    if weights[n - 1] > W:
        return knapsack_recursive(weights, values, W, n - 1)
    else:
        # 현재 물건 넣고 최대인지
        include = values[n - 1] + knapsack_recursive(
            weights, values, W - weights[n - 1], n - 1
        )
        # 현재 물건 안넣고 최대인지
        exclude = knapsack_recursive(weights, values, W, n - 1)
        return max(include, exclude)


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)
print(knapsack_recursive(weights, values, W, n))  # Output: 7
