n, m = map(int, input().split())
line = list(map(int, input().split()))
result = 0
for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            if line[i] + line[j] + line[k] <= m and i != j and i != k and j != k:
                if line[i] + line[j] + line[k] > result:
                    result = line[i] + line[j] + line[k]
print(result)
            