s = input()
pos = 0
num = 0
while pos < len(s):
    num += 1
    for ch in str(num):
        if pos < len(s) and ch == s[pos]:
            pos += 1
print(num)
