import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        print(heapq.heappop(heap) if heap else 0)
