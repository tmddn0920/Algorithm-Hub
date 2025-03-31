n, m = map(int, input().split())
arr = []
for i in range(0, n):
    arr.append(0)
for i in range(0, m):
    a, b, c = map(int, input().split())
    for j in range(a - 1, b):
        arr[j] = c
for num in range(0, len(arr)):
    print(arr[num], end=" ")