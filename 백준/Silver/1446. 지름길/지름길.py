from collections import defaultdict

n, dist = map(int, input().split())

dists = [i for i in range(dist + 1)]
short = defaultdict(list)

for _ in range(n):
    start, end, weight = map(int, input().split())

    if end <= dist and weight < end - start:
        short[start].append((end, weight))
        
        
for i in range(dist):
    dists[i + 1] = min(dists[i + 1], dists[i] + 1)
    if i in short:
        for e, w in short[i]:
            dists[e] = min(dists[e], dists[i] + w)

print(dists[dist])