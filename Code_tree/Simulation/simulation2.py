"""
행복한 수열의 개수

1이상 100이하의 숫자로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다.
이때 행복한 수열이라는 것은 다음과 같이 정의됩니다.
행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n과 연속해야 하는 숫자의 수를 나타내는 m이 공백을 사이에 두고 주어집니다.
두 번째 줄부터는 n개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며, 이 정보는 1이상 100이하의 숫자가 각각 공백을 사이에 두고 주어집니다.
1 ≤ m ≤ n ≤ 100

출력 형식
2n개의 수열들 중 행복한 수열의 수를 출력해주세요.

입출력 예제
입력:
3 2
1 2 2
1 3 4
1 2 3

출력:
2
"""
n, m = map(int, input().split())

answer = []
for _ in range(n):
    answer.append(list(map(int, input().split())))
check_list = [0 for _ in range(n)]

def check(check_list):
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, n):
        if check_list[i - 1] == check_list[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1

        max_ccnt = max(max_ccnt, consecutive_count)
    return max_ccnt >= m



count = 0
for i in range(n):
    check_list = answer[i]
    if check(check_list):
        count += 1
for i in range(n):
    for j in range(n):
        # check_list[j] = answer[j][i] 해당 코드에서 answer 값이 바뀌는 에러 발생 -> check_list와 answer 값이 같은 값을 참조하고 있기 때문에 변경 발생
        column_list = [answer[j][i] for j in range(n)]
    if check(column_list):
        count += 1

print(count)