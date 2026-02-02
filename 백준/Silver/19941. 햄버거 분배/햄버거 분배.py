n, k = map(int, input().split())

table = list(input())

answer = 0

for i in range(n):
    if table[i] == "H":
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and table[j] == "P":
                table[i] = 0
                table[j] = 0
                answer += 1
                # print(table)
                break

print(answer)
        