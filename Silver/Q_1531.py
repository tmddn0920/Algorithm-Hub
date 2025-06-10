N, M = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    X, Y, x, y = map(int, input().split())
    for i in range(Y - 1, y):
        for j in range(X - 1, x):
            arr[i][j] += 1
count = 0
for row in arr:
    for num in row:
        if num > M:
            count += 1
print(count)