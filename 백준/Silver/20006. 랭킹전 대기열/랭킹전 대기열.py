from collections import defaultdict

p, m = map(int, input().split())

room = defaultdict(list)
flag = False

for j in range(p):
    lv, id = input().split()
    lv = int(lv)

    for level, r in room.keys():
        if level - 10 <= lv <= level + 10 and len(room[(level, r)]) < m:
            room[((level, r))].append((lv, id))
            flag = True
            break
    if not flag:
        room[(lv, j)].append((lv, id))
    flag = False

# print(room)
room = dict(sorted(room.items(), key=lambda x:x[0][1]))

for v in room.values():
    if v:
        v = sorted(v, key=lambda x: x[1]) 
        if len(v) == m:
            print("Started!")
            for level, player in v:
                print(level, player)
        else:
            print("Waiting!")
            for level, player in v:
                print(level, player)
        