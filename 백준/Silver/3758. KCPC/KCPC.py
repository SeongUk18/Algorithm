from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k, id, m = map(int, input().split())
    score_dict = defaultdict(list)

    for c in range(m):
        i, j, s = map(int, input().split())
        if score_dict[(i,j)]:
            if score_dict[(i,j)][0] <= s:
                score_dict[(i,j)] = [s, score_dict[(i,j)][1] + 1, c]
            else:
                score_dict[(i,j)] = [score_dict[(i,j)][0], score_dict[(i,j)][1] + 1, c]
        else:
            score_dict[(i,j)] = [s, 1, c]

    # print(score_dict)
    teams = defaultdict(lambda: [0, 0, 0])

    for (team_id, problem), (score, cnt, time) in score_dict.items():
        teams[team_id][0] += score
        teams[team_id][1] += cnt
        teams[team_id][2] = max(teams[team_id][2], time)

    ranking = sorted(teams.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))

    # print(ranking)
    for idx, rank in enumerate(ranking):
        if rank[0] == id:
            print(idx + 1)
            break
