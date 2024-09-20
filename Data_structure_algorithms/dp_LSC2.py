def lcs(A, B):
    n, m = len(A), len(B)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 최장 공통 부분 수열 추적
    lcs_string = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs_string.append(A[i - 1])  # 공통 문자 찾음
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_string))  # 역추적 결과를 뒤집어서 반환


# 테스트
A = "ABCBDAB"
B = "BDCAB"
print(lcs(A, B))  # Output: "BDAB"
