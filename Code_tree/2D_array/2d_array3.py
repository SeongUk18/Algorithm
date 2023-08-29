"""
지그재그로 숫자 채우기

n * m크기의 직사각형에 숫자를 0부터 순서대로 1씩 증가시키며 왼쪽 위에서부터 시작하여  지그재그 모양으로 숫자들을 쭉 채우는 코드를 작성해보세요.

입력 형식
n과 m이 공백을 사이에 두고 주어집니다.
1 ≤ n, m ≤ 100

출력 형식
숫자로 채워진 완성된 형태의 n * m 크기의 사각형을 출력합니다. (숫자끼리는 공백을 사이에 두고 출력합니다.)

입출력 예제

입력:
4 2

출력:
0 7
1 6
2 5
3 4
"""

n, m = map(int, input().split())

num_list = [[0 for _ in range(m)]for _ in range(n)]

num = 0
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            if j % 2 == 0 or n == 1:
                num_list[j][i] = num
                num += 1
            else:
                num_list[j][i] = num
                num += 1
    else:
        for j in reversed(range(n)):
            if j % 2 == 0:
                num_list[j][i] = num
                num += 1
            else:
                num_list[j][i] = num
                num += 1


for i in range(n):
    for j in range(m):
        print(num_list[i][j], end=" ")
    print()
