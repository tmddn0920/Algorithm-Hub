import sys
input = sys.stdin.readline

memo = [(1, 0), (0, 1)] + [(-1, -1)] * 39

def fibonacci(n):
    if memo[n] != (-1, -1):
        return memo[n]
    a = fibonacci(n - 1)
    b = fibonacci(n - 2)
    memo[n] = (a[0] + b[0], a[1] + b[1])
    return memo[n]

num = int(input())
for _ in range(num):
    case = int(input())
    zero, one = fibonacci(case)
    print(f"{zero} {one}")