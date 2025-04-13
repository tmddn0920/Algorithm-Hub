a, b, v = map(int, input().split())
days = (v - b - 1) // (a - b) + 1
print(days)
    