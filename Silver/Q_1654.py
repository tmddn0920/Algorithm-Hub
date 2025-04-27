import sys

k, n = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]

left = 1  
right = max(arr)  

answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(x // mid for x in arr)
    
    if count >= n:
        answer = mid  
        left = mid + 1
    else:
        right = mid - 1

print(answer)