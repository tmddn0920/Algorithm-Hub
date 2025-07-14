import sys
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
A = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
distance = [sys.maxsize] * (V + 1)
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    A[u].append((v, w))

q.put((0, K))
distance[K] = 0

while q.qsize() > 0:
    temp = q.get()
    temp_v = temp[1]
    if visited[temp_v]:
        continue
    visited[temp_v] = True
    for i in A[temp_v]:
        next_v = i[0]
        next_weight = i[1]
        if distance[next_v] > distance[temp_v] + next_weight:
            distance[next_v] = distance[temp_v] + next_weight
            q.put((distance[next_v], next_v))
            
for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")