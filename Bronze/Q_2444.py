num = int(input())
for i in range(0, num):
    print(' ' * (num - i - 1), end="")
    print('*' * (2 * i + 1))
for i in range(1, num):
    print(' ' * i, end="")
    print('*' * (2 * (num - i) - 1))