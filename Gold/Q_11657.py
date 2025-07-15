import sys

N, M = map(int, input().split())
Arr = []
distance = [sys.maxsize] * (N + 1)

for i in range(M):
    A, B, C = map(int, input().split())
    Arr.append((A, B, C))
    
distance[1] = 0

for _ in range(N - 1):
    for start, end, time in Arr:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time
            
isInf = False

for start, end, time in Arr:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        isInf = True
    
if isInf:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])