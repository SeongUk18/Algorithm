import heapq

n = int(input())

pq = []

for _ in range(n):
    for num in map(int, input().split()):
        heapq.heappush(pq, num)
        if len(pq) > n:
            heapq.heappop(pq)

print(pq[0])
