"""
대각선으로 숫자 채우기

n * m크기의 직사각형에 숫자를 1부터 순서대로 1씩 증가시키며 왼쪽 위에서부터 시작하여 오른쪽 아래 쪽까지 같은 방향으로 숫자들을 쭉 채우는 코드를 작성해보세요.

입력 형식
n과 m이 공백을 사이에 두고 주어집니다.
1 ≤ n, m ≤ 100

출력 형식
숫자로 채워진 완성된 형태의 n * m 크기의 사각형을 출력합니다.
(숫자끼리는 공백을 사이에 두고 출력합니다.)

입출력 예제

입력:
3 3

출력:
1 2 4
3 5 7
6 8 9
"""
n, m = map(int, input().split())

num_list = [[0 for _ in range(m)]for _ in range(n)]

#### 풀다가 틀린 코드 ####
# num = 1
# i = 0
# j = 0
# count = 1
# num_list[i][j] = num
# num += 1
# j = count
# while count <= n + 1:
#     for _ in range(count + 1):
#         if 0 <= i < n and 0 <= j < m:
#             num_list[i][j] = num
#             j -= 1
#             i += 1
#             num += 1
#         else:
#             break
#     if count >= n:
#         j = count
#         i = count - 1
#         count += 1
#     else:
#         count += 1
#         j = count
#         i = 0

# step 1
count = 1
for start_col in range(m):
    curr_row = 0
    curr_col = start_col

    while 0 <= curr_col and curr_row < n:
        num_list[curr_row][curr_col] = count

        # 변수 업데이트
        curr_row += 1
        curr_col -= 1
        count += 1

# step 2
for start_row in range(1, n):
    curr_row = start_row
    curr_col = m - 1

    while 0 <= curr_col and curr_row < n:
        num_list[curr_row][curr_col] = count

        # 변수 업데이트
        curr_row += 1
        curr_col -= 1
        count += 1

for i in range(n):
    for j in range(m):
        print(num_list[i][j], end=" ")
    print()