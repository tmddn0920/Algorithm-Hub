n, B, C = map(int, input().split())
arr = list(map(int, input().split()))
cost = 0
i = 0

if B > C:
    
    while i < n:
        if i + 2 < n and arr[i + 1] > arr[i + 2]:
            m = min(arr[i], arr[i + 1] - arr[i + 2])
            arr[i] -= m
            arr[i + 1] -= m
            cost += (B + C) * m
    
        if i + 2 < n:
            m = min(arr[i], arr[i + 1], arr[i + 2])
            arr[i] -= m
            arr[i + 1] -= m
            arr[i + 2] -= m
            cost += (B + C + C) * m
    
        if i + 1 < n:
            m = min(arr[i], arr[i + 1])
            arr[i] -= m
            arr[i + 1] -= m
            cost += (B + C) * m
    
        cost += arr[i] * B
        arr[i] = 0
        i += 1
        
    print(cost)
    
elif B <= C:
    
    for num in arr:
        cost += num * B
        
    print(cost)        