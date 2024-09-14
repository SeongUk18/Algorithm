def solution(triangle):
    answer = 0
    # dp 생성
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    # dp 채우기
    for i in range(1, len(dp)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])

    # print(dp)
    # print(max(dp[len(triangle) - 1]))
    answer = max(dp[len(triangle) - 1])
    return answer
