def lcs(A, B):
    n, m = len(A), len(B)
    # DP 테이블 초기화 (0으로 채움)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # 두 문자가 같으면 1 증가
            else:  # 그렇지 않으면 이전 최댓값 유지
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]  # 최종적으로 dp[n][m]이 LCS의 길이를 저장


# 테스트
A = "ABCBDAB"
B = "BDCAB"
print(lcs(A, B))  # Output: 4 ("BDAB")
