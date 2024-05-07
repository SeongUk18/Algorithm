dic = {0: 0, 1: 1, 2: 1}


def fibo(x):
    if x in dic:
        return dic[x]
    else:
        dic[x] = fibo(x-1)+fibo(x-2)
        return dic[x]


n = int(input())
print(fibo(n))