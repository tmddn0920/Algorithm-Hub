num = int(input())

def sum_function(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return sum_function(n - 1) + sum_function(n - 2) + sum_function(n - 3)

for i in range(num):
    number = int(input())
    print(sum_function(number))