import sys
import heapq

n = int(sys.stdin.readline())

num_list = []


for _ in range(n):
    chk = int(sys.stdin.readline())

    if chk == 0:
        if num_list:
            print(heapq.heappop(num_list)[1])
        else:
            print(0)
    else:
        heapq.heappush(num_list, (abs(chk),chk)) # 튜플 형태로 우선순위 Q에 저장

