from collections import Counter

s = input()
s = list(s)
c = Counter(s)
one = c.get("1")
zero = c.get("0")

one_total = 0
zero_total = 0
for i in range(len(s)):
    if s[i] == "1":
        s[i] = "-"
        one_total += 1

    if one_total == one // 2:
        break

for i in range(len(s)- 1, -1, -1):
    if s[i] == "0":
        s[i] = "-"
        zero_total += 1

    if zero_total == zero // 2:
        break

answer = ""
for i in range(len(s)):
    if s[i] == "-":
        continue
    else:
        answer += s[i]

print(answer)