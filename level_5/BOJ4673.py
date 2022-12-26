numbers = [_ for _ in range(1, 10001)]


def d(number):
    number_1000 = number // 1000
    number_100 = (number-number_1000*1000) // 100
    number_10 = (number-number_1000*1000-number_100*100) // 10
    number_1 = number-number_1000*1000-number_100*100-number_10*10
    new_number = number + number_1000 + number_100 + number_10 + number_1
    if new_number in numbers:
        numbers.remove(new_number)


for i in range(1, 10001):
    d(i)

for result in numbers:
    print(result)
