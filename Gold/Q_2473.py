N = int(input())
A = list(map(int, input().split()))
A.sort()
total = 10**10
result = (0, 0, 0)

for i in range(N - 2):
    l = i + 1
    r = N - 1
    while l < r:
        temp = A[i] + A[l] + A[r]
        if abs(temp) < abs(total):
            total = temp
            result = (A[i], A[l], A[r])
            if total == 0:
                break
        if temp > 0:
            r -= 1
        elif temp < 0:
            l += 1

print(result[0], result[1], result[2])