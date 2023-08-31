"""
격자 반대로 채우기

n x n 크기의 격자에 정수를 채워넣으려고 합니다. 1부터 시작해서 차례대로 n^2까지 채워넣는데, 오른쪽 아래에서 부터 위 아래 지그재그 방향으로 채워넣는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에 격자의 크기에 해당하는 정수 n이 주어집니다.
1 ≤ n ≤ 10
출력 형식

첫 번째 줄부터 n개의 줄에 걸쳐, 각 행에 해당하는 n개의 숫자를 공백을 사이에 두고 출력합니다.

입출력 예제

입력:
4

출력:
13 12 5 4
14 11 6 3
15 10 7 2
16 9 8 1
"""
n = int(input())

answer = [[0 for _ in range(n)]for _ in range(n)]

num = 1
cur_row = n
cur_col = n-1
for _ in range(n):
    if cur_row <= 0:
        cur_row = -1
        for i in range(n):
            cur_row += 1
            answer[cur_row][cur_col] = num
            num += 1
    else:
        cur_row = n
        for i in range(n):
            cur_row -= 1
            answer[cur_row][cur_col] = num
            num += 1
    cur_col -= 1

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()
