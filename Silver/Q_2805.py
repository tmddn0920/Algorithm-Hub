N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for height in arr:
        if height > mid:
            total += height - mid

    if total >= M:
        answer = mid    
        start = mid + 1
    else:
        end = mid - 1   

print(answer)