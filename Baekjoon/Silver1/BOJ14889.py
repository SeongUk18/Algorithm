from itertools import combinations

n = int(input())

state = []

for _ in range(n):
    state.append(list(map(int, input().split())))

having = [False for _ in range(n)]
min_cost = float("inf")

for team in combinations(range(n), n // 2):
    s_team = list(team)
    l_team = [i for i in range(n) if i not in s_team]

    s_score = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            s_score += state[s_team[i]][s_team[j]] + state[s_team[j]][s_team[i]]

    l_score = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            l_score += state[l_team[i]][l_team[j]] + state[l_team[j]][l_team[i]]

    diff = abs(s_score - l_score)
    min_cost = min(min_cost, diff)

print(min_cost)
