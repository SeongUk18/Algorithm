"""
아래로 사각형 채우기

정사각형 한 변의 길이 n이 주어지면 아래 예와 같이 숫자로 된 정사각형 형태로 출력하는 프로그램을 작성해보세요.
예)
n에 3이 주어지는 경우
1 4 7
2 5 8
3 6 9
n에 4가 주어지는 경우
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16

입력 형식
첫번째 줄에 n이 주어집니다.
1 ≤ n ≤ 10

출력 형식
주어지는 n의 값에 따른 숫자로 된 정사각형을 입출력 예제와 같이 출력합니다.

입출력 예제
입력:
5

출력:
1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25
"""
n = int(input())

num_list = [[0 for _ in range(n)]for _ in range(n)]

num = 1

for i in range(n):
    for j in range(n):
        num_list[j][i] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(num_list[i][j], end=" ")
    print()

