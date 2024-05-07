from collections import deque
import sys

n = int(sys.stdin.readline())


def VPS_check():
    q = deque()
    VPS = sys.stdin.readline()
    for chk in VPS:
        if chk == "(":
            q.append(chk)
        elif chk == ")":
            if q:
                q.pop()
            else:
                q.append(0) # 처음에 ) 가 나왔을 때,
                break
    if q:
        print("NO")
        return
    else:
        print("YES")
        return


for _ in range(n):
    VPS_check()