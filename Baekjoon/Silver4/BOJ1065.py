N = int(input())
numbers = [_ for _ in range(1, N+1)]


def han_su(number):
    number_100 = number // 100
    number_10 = (number-number_100*100) // 10
    number_1 = number-number_100*100-number_10*10
    if number_100 == 0:
        return 0
    dist = number_100 - number_10
    if dist != number_10-number_1:
        if number in numbers:
            numbers.remove(number)


for i in range(1, N+1):
    han_su(i)
print(len(numbers))
