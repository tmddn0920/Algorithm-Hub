n = int(input())
arr = list(map(int, input().split()))
cost = 0
i = 0

while i < n:
    if i + 2 < n and arr[i + 1] > arr[i + 2]:
        m = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= m
        arr[i + 1] -= m
        cost += 5 * m

    if i + 2 < n:
        m = min(arr[i], arr[i + 1], arr[i + 2])
        arr[i] -= m
        arr[i + 1] -= m
        arr[i + 2] -= m
        cost += 7 * m

    if i + 1 < n:
        m = min(arr[i], arr[i + 1])
        arr[i] -= m
        arr[i + 1] -= m
        cost += 5 * m

    cost += arr[i] * 3
    arr[i] = 0
    i += 1

print(cost)