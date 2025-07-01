N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = int((start + end) / 2)
    total = 0
    count = 0
    for i in range(N):
        if total + A[i] > mid:
            count += 1
            total = 0
        total += A[i]
    if total != 0:
        count += 1
    if count > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)