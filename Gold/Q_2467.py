N = int(input())
A = list(map(int, input().split()))
total = 10**10
l, r = 0, N - 1
result = (A[l], A[r])

while l < r:
    temp = A[l] + A[r]
    if abs(temp) < abs(total):
        total = temp
        result = (A[l], A[r])
        if total == 0:
            break
    if temp > 0:
        r -= 1
    elif temp < 0:
        l += 1

print(result[0], result[1])