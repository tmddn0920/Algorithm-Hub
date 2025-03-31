n, m = map(int, input().split())
arr = []
for i in range(0, n):
    arr.append(i + 1)
for i in range(0, m):
    a, b = map(int, input().split())
    temp = arr[a - 1]
    arr[a - 1] = arr[b - 1]
    arr[b - 1] = temp
for num in range(0, len(arr)):
    print(arr[num], end=" ")
