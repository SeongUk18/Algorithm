from collections import defaultdict

# 입력 받기
n = int(input())

# 갈수 있는곳 넣는 용
search_dict = defaultdict(list)

for i in range(n):
    road_list = list(map(int, input().split()))

    for j in range(len(road_list)):
        # 가중치가 0이면 길이 없음
        if road_list[j] == 0:
            continue

        # 연결된 부분 연결된곳, 가중치 값으로 저장
        search_dict[i].append((j, road_list[j]))

# print(search_dict)
# 방문 확인용
is_visited = [False for _ in range(n)]
# 결과 저장용
answer = []


# 완탐
def dfs(n, road, city, weights, start):
    if city == n:  # 도시를 다 돌았을때
        # 다시 돌아갈 수 있는지 확인
        for i, weight in search_dict[road]:
            if i == start:
                answer.append(weights + weight)
        return

    is_visited[road] = True

    for i, weight in search_dict[road]:
        # print(i)
        # print(weight)
        if is_visited[i] == False:
            # 다음 도시 이동
            dfs(n, i, city + 1, weights + weight, start)

    # 백트래킹
    is_visited[road] = False


dfs(n, 0, 1, 0, 0)
print(min(answer))
