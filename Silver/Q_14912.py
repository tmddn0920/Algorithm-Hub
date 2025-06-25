N, D = map(int, input().split())
count = 0
for Num in range(1, N + 1):
    Arr = list(str(Num))
    for Number in Arr:
        if int(Number) == D:
            count += 1
print(count)