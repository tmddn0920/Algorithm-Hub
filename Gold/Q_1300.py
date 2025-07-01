N = int(input())
k = int(input())
start = 1
end = k
result = 0

while start <= end:
    mid = int((start + end) / 2)
    count = 0
    for i in range(1, N + 1):
        count += min(int(mid / i), N)
    if count < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)