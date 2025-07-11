import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
A = [[]for _ in range(N + 1)]
A_Reverse = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    S, E, T = map(int, input().split())
    A[S].append((E, T))
    A_Reverse[E].append((S, T))
    degree[E] += 1
    
Start, End = map(int, input().split())

queue = deque()
queue.append(Start)
result = [0] * (N + 1)

while queue:
    temp = queue.popleft()
    for tup in A[temp]:
        degree[tup[0]] -= 1
        result[tup[0]] = max(result[tup[0]], result[temp] + tup[1])
        if degree[tup[0]] == 0:
            queue.append(tup[0])
            
count = 0
visited = [False] * (N + 1)
queue.clear()
queue.append(End)
visited[End] = True
count = 0

while queue:
    temp = queue.popleft()
    for tup in A_Reverse[temp]:
        if result[temp] == result[tup[0]] + tup[1]:
            count += 1
            if visited[tup[0]] == False:
                visited[tup[0]] = True
                queue.append(tup[0])
 
print(result[End])
print(count)