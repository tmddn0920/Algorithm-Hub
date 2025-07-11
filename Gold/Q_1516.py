from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
time = [0] * (N + 1)

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    num = 1
    while True:
        temp = arr[num]
        num += 1
        if temp == -1:
            break
        A[temp].append(i)
        degree[i] += 1
        
queue = deque()

for i in range(1, N + 1):
    if degree[i] == 0:
        queue.append(i)
        
result = [0] * (N + 1)

while queue:
    temp = queue.popleft()
    for i in A[temp]:
        degree[i] -= 1
        result[i] = max(result[i], result[temp] + time[temp])
        if degree[i] == 0:
            queue.append(i)
            
for i in range(1, N + 1):
    result[i] += time[i]
    print(result[i])