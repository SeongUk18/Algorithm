n, m = map(int, input().split())

map_list = []

for i in range(n):
    map_list.append(list(map(int, input().split())))

answer = float('inf')
dist = [-1, 0, 1]

def land(hight, oil, prv_dist, prv_pos, n, m):
    global answer

    if answer <= oil:
        return
    
    if hight == n:
        answer = min(answer, oil)
        return

    for i in range(3):
        if i == prv_dist:
            continue
                  

        elif 0 <= dist[i] + prv_pos < m:
            pos = prv_pos + dist[i]
            land(hight + 1, oil + map_list[hight][pos], i, pos, n, m)


    

for i in range(m):
    land(0, 0, -1, i, n, m)

print(answer)