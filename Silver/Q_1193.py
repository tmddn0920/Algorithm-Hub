num = int(input())
total = 1
number = 1
while True:
    if num <= total:
        break
    elif num > total:
        number += 1
        total += number
total -= number
if number % 2 == 0:
    print(num - total, end="")
    print('/', end="")
    print(number + 1 - num + total)
else:
    print(number + 1 - num + total, end="")
    print('/', end="")
    print(num - total)