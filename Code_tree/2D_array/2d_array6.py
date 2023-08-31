"""
배열로 사각형 만들기

배열을 만들어서 아래 조건을 만족해 출력하는 프로그램을 작성해보세요.
첫 번째 행과 첫 번째 열은 모두 1로 초기화 합니다.
나머지 칸들은 바로 위의 값과 바로 왼쪽의 값을 더합니다.
크기는 5 * 5 입니다.

입력 형식
입력이 주어지지 않습니다.

출력 형식
입출력 예제와 같이 출력합니다.

입출력 예제
입력:

출력:
1 1 1 1 1
1 2 3 4 5
1 3 6 10 15
1 4 10 20 35
1 5 15 35 70
"""
answer = [[0 for _ in range(5)]for _ in range(5)]

for i in range(5):
    answer[0][i] = 1

for i in range(1, 5):
    for j in range(5):
        if j == 0:
            answer[i][j] = 1
        else:
            answer[i][j] = answer[i-1][j] + answer [i][j-1]

for i in range(5):
    for j in range(5):
        print(answer[i][j], end=" ")
    print()